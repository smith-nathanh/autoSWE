from typing import Any, List, Dict, Type, Union, Literal, Annotated
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START, END
from system.prompts import *
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, AnyMessage
import logging
from copy import deepcopy
from langchain_openai import ChatOpenAI
import subprocess
from system.utils import check_and_install_packages, create_repository
from system.structure import (GraphState, 
                       Design, 
                       ApproveDesign, 
                       EnvironmentSetup, 
                       Implementation, 
                       ApproveImplementation,
                       AcceptanceTests,
                       UnitTests)
from system.tools import (view_document,update_document,add_document,delete_document)

# need to find better place for this, I believe this can be specified in a config
llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
#llm = ChatAnthropic(model_name='claude-3-5-sonnet-20241022', temperature=0)

# *** we need a subgraph to rerun acceptance and unit tests after a change has been made to the implementation

# update messages at each node
# let the llm choose to call a tool or to call the respond tool format the respond tool 
# uniquely for each task so that we get structured outputs each time
def software_design_condition(
    state: Union[list[AnyMessage], dict[str, Any], BaseModel],
    messages_key: str = "messages",
) -> Literal["tools", "approve_software_design"]:
    """Use in the conditional_edge to route to the ToolNode if the last message

    has tool calls. Otherwise, route to the end.

    Args:
        state (Union[list[AnyMessage], dict[str, Any], BaseModel]): The state to check for
            tool calls. Must have a list of messages (MessageGraph) or have the
            "messages" key (StateGraph).

    Returns:
        The next node to route to.
    """
    if isinstance(state, list):
        ai_message = state[-1]
    elif isinstance(state, dict) and (messages := state.get(messages_key, [])):
        ai_message = messages[-1]
    elif messages := getattr(state, messages_key, []):
        ai_message = messages[-1]
    else:
        raise ValueError(f"No messages found in input state to tool_edge: {state}")
    if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
        return "tools"
    return "approve_software_design"

def implementation_condition(
    state: Union[list[AnyMessage], dict[str, Any], BaseModel],
    messages_key: str = "messages",
) -> Literal["tools", "approve_implementation"]:
    """Use in the conditional_edge to route to the ToolNode if the last message

    has tool calls. Otherwise, route to the end.

    Args:
        state (Union[list[AnyMessage], dict[str, Any], BaseModel]): The state to check for
            tool calls. Must have a list of messages (MessageGraph) or have the
            "messages" key (StateGraph).

    Returns:
        The next node to route to.
    """
    if isinstance(state, list):
        ai_message = state[-1]
    elif isinstance(state, dict) and (messages := state.get(messages_key, [])):
        ai_message = messages[-1]
    elif messages := getattr(state, messages_key, []):
        ai_message = messages[-1]
    else:
        raise ValueError(f"No messages found in input state to tool_edge: {state}")
    if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
        return "tools"
    return "approve_implementation"


def assistant(state: GraphState):
    """
    The assistant helps the user to fix the documents based on the reviewer's feedback.
    """
    logging.info("---ASSISTANT---")
    sys_message = SystemMessage(content=
                                """
                                Please fix the documents based on the reviewer's feedback.
                                You must use the tools available to you to make changes to the state of the documents.
                                Don't perform any changes outside of the tools.
                                """)
    llm_with_tools = llm.bind_tools([view_document, update_document, add_document, delete_document])
    state['messages'] = [llm_with_tools.invoke([sys_message] + [state['messages'][-1]])]
    return state

def software_design(state: GraphState):
    """
    Designs the markdown files for the software design.
    """
    logging.info("---SOFTWARE DESIGN---")
    prompt = state['messages']
    if 'approvals' in state:
        if not all(state["approvals"].values()):
            prompt = [
            SystemMessage(content="You are a helpful assistant. Generate improved content based on the original request and reviewer feedback."),
            HumanMessage(content=DESIGN_PROMPT.format(PRD=state["documents"]['PRD'])),
            HumanMessage(content=f"Your previous response needed improvement. Here's the reviewer feedback:\n{state['messages'][-1].content}\n\nPlease generate an improved version addressing these specific issues.")
            ]
    structured_llm = llm.with_structured_output(Design)
    response = structured_llm.invoke(prompt)
    state["documents"].update(response.dict())
    return state

def approve_software_design(state: GraphState):
    """
    LLM-as-a-judge to review the design documents.
    """
    logging.info("---APPROVE SOFTWARE DESIGN---")
    prompt = APPROVE_DESIGN_PROMPT.format(**state['documents'])
    structured_llm = llm.with_structured_output(ApproveDesign)
    approval = structured_llm.invoke([HumanMessage(content=prompt)])
    # temporarily using hardcoded values
    state['approvals'] = {"UML_class": approval.UML_class,
                          "UML_sequence": approval.UML_sequence, 
                          "architecture_design": approval.architecture_design}
    state['messages'].append(approval.message)
    return state

def route_software_design(state: GraphState) -> Literal['implementation', 'software_design']:
    if all(state["approvals"].values()):
        return "implementation"
    else:
        return "software_design"

def implementation(state: GraphState):
    """
    Implement the software design.
    """
    logging.info("---IMPLEMENTATION---")
    prompt = [HumanMessage(content=IMPLEMENTATION_PROMPT.format(**state["documents"]))]
    if 'implementation' in state['approvals']:
        if not state['approvals']['implementation']:
            prompt = [
            SystemMessage(content="You are a helpful assistant. Generate improved content based on the original request and reviewer feedback."),
            prompt[-1],
            HumanMessage(content=f"Your previous response needed improvement. Here's the reviewer feedback:\n{state['messages'][-1].content}\n\nPlease generate an improved version addressing these specific issues.")
            ]
    structured_llm = llm.with_structured_output(Implementation)
    code = structured_llm.invoke(prompt)
    state["messages"].append(prompt)
    state['documents'].update(code.dict())
    return state

def approve_implementation(state: GraphState):
    logging.info("---APPROVE IMPLEMENTATION---")
    prompt = APPROVE_IMPLEMENTATION_PROMPT.format(architecture_design=state["documents"]['architecture_design'],
                                                  code=list(state["documents"]['code'].keys()))
    state['messages'].append(HumanMessage(content=prompt))
    structured_llm = llm.with_structured_output(ApproveImplementation)
    approval = structured_llm.invoke([HumanMessage(content=prompt)])
    state['approvals'].update({"implementation": approval.implementation})
    state['messages'].append(AIMessage(content=approval.message))
    return state

def route_implementation(state: GraphState) -> Literal['acceptance_tests', 'implementation']:
    if all(state["approvals"].values()):
        return "acceptance_tests"
    else:
        return "implementation"

def acceptance_tests(state: GraphState):
    """
    Generate acceptance tests for the software.
    """
    logging.info("---ACCEPTANCE TESTS---")
    code = '\n\n'.join(f"# ---{filename}---\n{content}" 
                       for filename, content in state['documents']['code'].items())
    prompt = ACCEPTANCE_TEST_PROMPT.format(PRD=state["documents"]['PRD'],
                                           architecture_design=state["documents"]['architecture_design'],
                                           code=code)
    structured_llm = llm.with_structured_output(AcceptanceTests)
    test = structured_llm.invoke([HumanMessage(content=prompt)])
    state["documents"].update(test.dict())
    return state

def approve_acceptance_tests(state: GraphState):
    logging.info("---APPROVE ACCEPTANCE TESTS---")
    
    try:
        root_dir = next(iter(state['documents']['code'])).split('/')[0]
        cmd = f"cd temp/{root_dir} && {state['documents']['acceptance_tests']['command']}"
        # Run command in shell, capture output
        process = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Add command to messages
        state['messages'].append(state['documents']['acceptance_tests']['command'])
        
        # Check return code
        if process.returncode == 0:
            state['approvals'].update({"acceptance_tests": True})
            state['messages'].append(f"Acceptance tests passed: \n{process.stdout}")
        else:
            state['approvals'].update({"acceptance_tests": False})
            state['messages'].append(f"Acceptance tests failed: \n{process.stdout}")
            
    except Exception as e:
        state['approvals'].update({"acceptance_tests": False})
        state['messages'].append(f"Error running acceptance tests: {str(e)}")
        
    return state

def route_acceptance_tests(state: GraphState) -> Literal['approve_unit_tests', 'assistant']:
    if all(state["approvals"].values()):
        return "approve_unit_tests"
    else:
        return "assistant" # go back to implementation with a message from the controller

def unit_tests(state: GraphState):
    """
    Generate unit tests for the software.
    """
    logging.info("---UNIT TESTS---")
    state['approvals']['unit_tests_iter'] = state['approvals'].get('unit_tests_iter', 0) + 1
    
    code = '\n\n'.join(f"# ---{filename}---\n{content}" 
                       for filename, content in state['documents']['code'].items())
    prompt = [HumanMessage(content=UNIT_TEST_PROMPT.format(PRD=state["documents"]['PRD'],
                                           architecture_design=state["documents"]['architecture_design'],
                                           code=code))]
    if 'unit_tests' in state['approvals']:
        if not state['approvals']['unit_tests_coverage']:
            prompt = [
            SystemMessage(content="You are a helpful assistant. Generate improved content based on the original request and reviewer feedback."),
            prompt[-1],
            HumanMessage(content=f"Your previous response needed improvement. Here's the reviewer feedback:\n{state['messages'][-1]}\n\nPlease generate an improved version addressing these specific issues.")
            ]
    structured_llm = llm.with_structured_output(UnitTests)
    test = structured_llm.invoke(prompt)
    state["documents"].update(test.dict())
    return state

def approve_unit_tests(state: GraphState):
    logging.info("---APPROVE UNIT TESTS---")

    # Get first directory name, handling paths with leading slash
    root_dir = next(name for name in next(iter(state['documents']['code'])).split('/') if name)
    cmd = f"cd temp/{root_dir} && {state['documents']['unit_tests']['command'].replace('python ', 'coverage run ')}"

    try:
        # Run command in shell, capture output
        process = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Add command to messages
        state['messages'].append(cmd)
        
        # Check return code
        if process.returncode == 0:
            state['approvals'].update({"unit_tests": True})
            state['messages'].append(f"Unit tests passed: \n{process.stdout}")
        else:
            state['approvals'].update({"unit_tests": False})
            state['messages'].append(f"Unit tests failed: \n{process.stdout}")
        
        # Run coverage report
        coverage_cmd = f"cd temp/{root_dir} && coverage report"
        coverage_process = subprocess.run(
            coverage_cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Add coverage command to messages
        state['messages'].append(coverage_cmd)
        
        if coverage_process.returncode == 0:
            # Parse coverage report output
            coverage_output = coverage_process.stdout
            #state['messages'].append(coverage_output)
            
            # Extract total coverage percentage
            for line in coverage_output.splitlines():
                if line.startswith("TOTAL"):
                    total_coverage = int(line.split()[3].replace('%', ''))
                    if total_coverage < 60:
                        state['approvals'].update({"unit_tests_coverage": False})
                        msg = f"Unit tests failed to cover at least 60% please revise unit tests: \n{coverage_output}"
                        state['messages'].append(msg)
                        logging.info(msg)
                    else:
                        state['approvals'].update({"unit_tests_coverage": True})
                        msg = f"Coverage report successful: \n{coverage_output}"
                        state['messages'].append(msg)
                        logging.info(msg)
                    break
        else:
            msg = f"Coverage report failed execution: {coverage_process.stdout}"
            state['messages'].append(msg)
            logging.info(msg)
            state['approvals'].update({"unit_tests_coverage": False})
            
    except Exception as e:
        state['approvals'].update({"unit_tests": False, "unit_tests_coverage": False})
        msg = f"Error running unit tests: {str(e)}"
        state['messages'].append(msg)
        logging.info(msg)
        
    return state

def route_unit_tests(state: GraphState) -> Literal["__end__", 'unit_tests']:
    if state['approvals']['unit_tests_coverage'] or state['approvals']['unit_tests_iter'] > 2:
        return END
    else:
        return "unit_tests" # go back and regenerate unit tests

def environment_setup(state: GraphState):
    """
    Based on the design documents, determine the requirements.txt file.
    """
    logging.info("---ENVIRONMENT SETUP---")
    code = '\n'.join(state['documents']['code'].values())
    prompt = ENVIRONMENT_SETUP_PROMPT.format(code=code)
    structured_llm = llm.with_structured_output(EnvironmentSetup)
    reqs = structured_llm.invoke([HumanMessage(content=prompt)])
    state["documents"].update(reqs.dict())

    # check if the required packages are installed
    package_list = reqs.requirements.split('\n')
    results = check_and_install_packages(package_list)
    # Check if any package failed to install
    if any(pkg_result['installed'] == False for pkg_result in results.values()):
        failed_packages = [pkg for pkg, result in results.items() if result['installed'] == False]
        msg = f"Failed to install packages: {', '.join(failed_packages)}"
        msg += '\n'.join([f"{pkg}: {results[pkg]['message']}" for pkg in failed_packages])
        state['messages'].append(msg)
    
    # write out the files to the temp/ directory
    try:
        create_repository("temp", state['documents'])
    except Exception as e:
        state['messages'].append(f"Failed to create the repository: {str(e)}")
        raise e

    return state

def route_environment_setup(state: GraphState) -> Literal['approve_acceptance_tests', 'environment_setup']:
    if all(state["approvals"].values()):
        return "approve_acceptance_tests"
    else:
        return "environment_setup"


def build_graph():

    graph = StateGraph(GraphState)

    # nodes
    #graph.add_node('tools', ToolNode([view_document, update_document, add_document, delete_document]))
    #graph.add_node("assistant", assistant)
    graph.add_node("software_design", software_design)
    graph.add_node("approve_software_design", approve_software_design)
    graph.add_node("environment_setup", environment_setup)
    #graph.add_node("approve_environment_setup", approve_environment_setup)
    graph.add_node("implementation", implementation)
    graph.add_node("approve_implementation", approve_implementation)
    graph.add_node("acceptance_tests", acceptance_tests)
    graph.add_node("approve_acceptance_tests", approve_acceptance_tests)
    graph.add_node("unit_tests", unit_tests)
    graph.add_node("approve_unit_tests", approve_unit_tests)

    # edges
    graph.add_edge(START, "software_design")
    graph.add_edge("software_design", "approve_software_design")
    graph.add_conditional_edges("approve_software_design", route_software_design)
    graph.add_edge("implementation", "approve_implementation")
    graph.add_conditional_edges("approve_implementation", route_implementation)
    graph.add_edge("acceptance_tests", "unit_tests")
    graph.add_edge('unit_tests', "environment_setup")
    graph.add_edge("environment_setup", "approve_acceptance_tests")
    graph.add_edge("approve_acceptance_tests", "approve_unit_tests")
    graph.add_conditional_edges("approve_unit_tests", route_unit_tests)

    return graph.compile()