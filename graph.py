from typing import Any, List, Dict, Type, Union, Literal, Annotated
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from langchain.schema import Document
from langgraph.graph import StateGraph, START, END, MessagesState
from prompts import *
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, AnyMessage
import logging
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langgraph.prebuilt import InjectedState, ToolNode, ToolExecutor, tools_condition
from langchain_core.prompts import ChatPromptTemplate


# need to find better place for this, I believe this can be specified in a config
llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
#llm = ChatAnthropic(model_name='claude-3-5-sonnet-20241022', temperature=0)

# Define the state of our graph
class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """
    messages: List[str]
    approvals: Dict[str, bool]
    documents: Dict[str, Union[str, Dict[str, str]]]

# Defining the models for the structured outputs
class Design(BaseModel):
    UML_class: str = Field(description="UML class diagram using mermaid syntax")
    UML_sequence: str = Field(description="UML sequence diagram using mermaid syntax")
    architecture_design: str = Field(description="architecture design as a text based representation of the file tree")

class ApproveDesign(BaseModel):
    UML_class: bool
    UML_sequence: bool
    architecture_design: bool
    message: str

class EnvironmentSetup(BaseModel):
    requirements: str = Field(description="All the expected dependencies that can be written to a file named requirements.txt")

class Implementation(BaseModel):
    code: Dict[str, str]

class ApproveImplementation(BaseModel):
    implementation: bool
    message: str

class AcceptanceTests(BaseModel):
    acceptance_tests: str = Field(description="Acceptance test script for the software")

class UnitTests(BaseModel):
    unit_tests: str = Field(description="Unit test script for the software")

class UpdateDocument(BaseModel):
    content: str

# want the agent to be able to edit only one document at a time, don't want a regeneration from that node again
# so we use an assistant that has access to tools to fix documents based on feedback from the reviewer

@tool
def view_document(document_name: str, state: Annotated[dict, InjectedState]) -> str:
    """
    Retrieves a document for inspection/review. This tool is used by the assistant to view the document.
    """
    if document_name not in state["documents"]:
        if document_name not in state["documents"]["code"]:
            return "document not found"
        else:
            return state["documents"]["code"][document_name]
    return state["documents"][document_name]

@tool
def update_document(document_name: str, content: str, state: Annotated[dict, InjectedState]) -> GraphState:
    """
    Issue an update to a document. This tool is used by the assistant to update the document.
    """
    if document_name not in state["documents"]:
        if document_name not in state["documents"]["code"]:
            return "document not found"
        else:
            state["documents"]["code"][document_name] = content
    state["documents"][document_name] = content
    return state

@tool
def add_document(document_name: str, content: str, state: Annotated[dict, InjectedState]) -> GraphState:
    """
    Add a document. This tool is used by the assistant to add a new document.
    """
    if document_name not in state["documents"]:
        if document_name not in state["documents"]["code"]:
            return "document not found"
        else:
            state["documents"]["code"][document_name] = content
    state["documents"][document_name] = content
    return state

@tool
def delete_document(document_name: str, state: Annotated[dict, InjectedState]) -> GraphState:
    """
    Delete a document. This tool is used by the assistant to delete the document.
    """
    if document_name not in state["documents"]:
        if document_name not in state["documents"]["code"]:
            return "document not found"
        else:
            del state["documents"]["code"][document_name]
            return state
    del state["documents"][document_name]
    return state

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
    #response = structured_llm.invoke([HumanMessage(content=prompt)])
    #state["documents"].update(response.dict())
    #return state

def software_design(state: GraphState):
    """
    Designs the markdown files for the software design.
    """
    logging.info("---SOFTWARE DESIGN---")
    #prompt = DESIGN_PROMPT.format(**state['documents'])
    # state["messages"] = [HumanMessage(content=DESIGN_PROMPT.format(**state['documents']))]
    # if "approvals" in state:
    #     if not all(state['approvals'].values()): # this implies that we are back at this node after a rejection
    #         llm_with_tools = llm.bind_tools([view_document, update_document, add_document, delete_document])
    #         state['messages'] = [llm_with_tools.invoke([sys_message] + [state['messages'][-1]])]
    #         return state
    structured_llm = llm.with_structured_output(Design)
    response = structured_llm.invoke(state['messages']) #[HumanMessage(content=prompt)])
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

def route_software_design(state: GraphState) -> Literal['environment_setup', 'assistant']:
    if all(state["approvals"].values()):
        return "environment_setup"
    else:
        return "assistant"

def environment_setup(state: GraphState):
    """
    Based on the design documents, determine the requirements.txt file.
    """
    logging.info("---ENVIRONMENT SETUP---")
    prompt = ENVIRONMENT_SETUP_PROMPT.format(**state["documents"])
    structured_llm = llm.with_structured_output(EnvironmentSetup)
    reqs = structured_llm.invoke([HumanMessage(content=prompt)])
    state["documents"].update(reqs.dict())
    return state

def approve_environment_setup(state: GraphState):
    """
    Test the requirements.txt file.
    """
    logging.info("---APPROVE ENVIRONMENT SETUP---")
    # need a shell to run the requirements.txt file and see if it works
    state['approvals'].update({"requirements": True})
    return state

def route_environment_setup(state: GraphState) -> Literal['implementation', 'environment_setup']:
    if all(state["approvals"].values()):
        return "implementation"
    else:
        return "environment_setup"

def implementation(state: GraphState):
    """
    Implement the software design.
    """
    logging.info("---IMPLEMENTATION---")
    prompt = IMPLEMENTATION_PROMPT.format(**state["documents"])
    if 'implementation' in state['approvals']:
        if not state['approvals']['implementation']:
            prompt += state['messages'][-1] # add the message from the controller
    structured_llm = llm.with_structured_output(Implementation)
    state["messages"].append(HumanMessage(content=prompt))
    code = structured_llm.invoke([HumanMessage(content=prompt)])
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

def route_implementation(state: GraphState) -> Literal['acceptance_tests', 'assistant']:
    if all(state["approvals"].values()):
        return "acceptance_tests"
    else:
        return "assistant"

def acceptance_tests(state: GraphState):
    """
    Generate acceptance tests for the software.
    """
    logging.info("---ACCEPTANCE TESTS---")
    prompt = ACCEPTANCE_TEST_PROMPT.format(**state["documents"])
    structured_llm = llm.with_structured_output(AcceptanceTests)
    test = structured_llm.invoke([HumanMessage(content=prompt)])
    state["documents"].update(test.dict())
    return state

def approve_acceptance_tests(state: GraphState):
    logging.info("---APPROVE ACCEPTANCE TESTS---")
    # need a shell to run the acceptance tests and see if they pass
    # temporary response below
    state['approvals'].update({"acceptance_tests": True})
    state['messages'].append("Acceptance tests passed") # llm response message
    return state

def route_acceptance_tests(state: GraphState) -> Literal['unit_tests', 'implementation']:
    if all(state["approvals"].values()):
        return "unit_tests"
    else:
        return "implementation" # go back to implementation with a message from the controller

def unit_tests(state: GraphState):
    """
    Generate unit tests for the software.
    """
    logging.info("---UNIT TESTS---")
    prompt = UNIT_TEST_PROMPT.format(**state["documents"]
                                     # also pass the code here or maybe chunk it
                                     # maybe don't pass all the other documents, just the code not sure yet
                                     )
    structured_llm = llm.with_structured_output(UnitTests)
    test = structured_llm.invoke([HumanMessage(content=prompt)])
    state["documents"].update(test.dict())
    return state

def approve_unit_tests(state: GraphState):
    logging.info("---APPROVE UNIT TESTS---")
    # need a shell to run the unit tests and see if they pass
    # temporary response below
    state['approvals'].update({"unit_tests": True})
    state['messages'].append("Unit tests passed") # llm response message
    return state

def route_unit_tests(state: GraphState) -> Literal["__end__", 'implementation']:
    if all(state["approvals"].values()):
        return END
    else:
        return "implementation" # go back to implementation with a message from the controller

def build_graph():

    graph = StateGraph(GraphState)

    # nodes
    graph.add_node('tools', ToolNode([view_document, update_document, add_document, delete_document]))
    graph.add_node("assistant", assistant)
    graph.add_node("software_design", software_design)
    graph.add_node("approve_software_design", approve_software_design)
    graph.add_node("environment_setup", environment_setup)
    graph.add_node("approve_environment_setup", approve_environment_setup)
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
    #graph.add_conditional_edges("assistant", software_design_condition)
    graph.add_edge("environment_setup", "approve_environment_setup")
    graph.add_conditional_edges("approve_environment_setup", route_environment_setup)
    graph.add_edge("implementation", "approve_implementation")
    graph.add_conditional_edges("approve_implementation", route_implementation)
    graph.add_conditional_edges("assistant", implementation_condition)
    graph.add_edge("acceptance_tests", "approve_acceptance_tests")
    graph.add_conditional_edges("approve_acceptance_tests", route_acceptance_tests)
    graph.add_edge("unit_tests", "approve_unit_tests")
    graph.add_conditional_edges("approve_unit_tests", route_unit_tests)

    return graph.compile()