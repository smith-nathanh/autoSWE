from typing import Any, List, Dict, Type, Union, Literal
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from langchain.schema import Document
from langgraph.graph import StateGraph, START, END
from prompts import *
from langchain_core.messages import HumanMessage
import logging
from langchain_openai import ChatOpenAI

# need to find better place for this
llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

# Define the state of our graph
class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """
    prompt: str
    messages: List[str]
    approvals: Dict[str, bool]
    documents: Dict[str, Union[str, Document, Dict[str, str]]]

# Defining the models for the structured outputs
class Design(BaseModel):
    UML_class: str = Field(description="UML class diagram using mermaid syntax")
    UML_sequence: str = Field(description="UML sequence diagram using mermaid syntax")
    architecture_design: str = Field(description="architecture design as a text based representation of the file tree")

class Requirements(BaseModel):
    requirements: str = Field(description="All the expected dependencies that can be written to a file named requirements.txt")

class Implementation(BaseModel):
    code: Dict[str, str]

class AcceptanceTests(BaseModel):
    acceptance_tests: str = Field(description="Acceptance test script for the software")

class UnitTests(BaseModel):
    unit_tests: str = Field(description="Unit test script for the software")

def software_design(state: GraphState):
    """
    Designs the markdown files for the software design.
    """
    logging.info("---SOFTWARE DESIGN---")
    design_prompt = DESIGN_PROMPT.format(**state['documents'])
    structured_llm = llm.with_structured_output(Design)
    response = structured_llm.invoke([HumanMessage(content=design_prompt)])
    state["documents"].update(response.dict())
    return state

def approve_software_design(state: GraphState):
    """
    LLM-as-a-judge to review the design documents.
    """
    logging.info("------APPROVE SOFTWARE DESIGN---")
    prompt = APPROVE_DESIGN_PROMPT.format(**state['documents'])
    #approvals = llm.invoke([HumanMessage(content=prompt)]) # use structured outputs here
    # temporarily using hardcoded values
    state['approvals'] = {"UML_class": True, "UML_sequence": True, "architecture_design": True}
    state['messages'] = ["UML class diagram approved"] # llm reponse message
    return state

def route_software_design(state: GraphState) -> Literal['requirements', 'software_design']:
    if all(state["approvals"].values()):
        return "requirements"
    else:
        return "software_design"

def requirements(state: GraphState):
    """
    Based on the design documents, determine the requirements.txt file.
    """
    logging.info("---REQUIREMENTS---")
    prompt = REQUIREMENTS_PROMPT.format(**state["documents"])
    structured_llm = llm.with_structured_output(Requirements)
    reqs = structured_llm.invoke([HumanMessage(content=prompt)])
    state["documents"].update(reqs.dict())
    return state

def approve_requirements(state: GraphState):
    """
    Test the requirements.txt file.
    """
    logging.info("------APPROVE REQUIREMENTS---")
    # need a shell to run the requirements.txt file and see if it works
    state['approvals'].update({"requirements": True})
    return state

def route_requirements(state: GraphState) -> Literal['implementation', 'requirements']:
    if all(state["approvals"].values()):
        return "implementation"
    else:
        return "requirements"

def implementation(state: GraphState):
    """
    Implement the software design.
    """
    logging.info("---IMPLEMENTATION---")
    prompt = IMPLEMENTATION_PROMPT.format(**state["documents"])
    structured_llm = llm.with_structured_output(Implementation)
    code = structured_llm.invoke([HumanMessage(content=prompt)])
    state['documents'].update(code.dict())
    return state

def approve_implementation(state: GraphState):
    logging.info("------APPROVE IMPLEMENTATION---")
    # need a shell to run the code and see if it works
    # run pylint on the code
    # temporary response below
    state['approvals'].update({"implementation": True})
    state['messages'].append("Code approved") # llm response message
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
    prompt = ACCEPTANCE_TEST_PROMPT.format(**state["documents"])
    structured_llm = llm.with_structured_output(AcceptanceTests)
    test = structured_llm.invoke([HumanMessage(content=prompt)])
    state["documents"].update(test.dict())
    return state

def approve_acceptance_tests(state: GraphState):
    logging.info("------APPROVE ACCEPTANCE TESTS---")
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
    logging.info("------APPROVE UNIT TESTS---")
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
    graph.add_node("software_design", software_design)
    graph.add_node("approve_software_design", approve_software_design)
    graph.add_node("requirements", requirements)
    graph.add_node("approve_requirements", approve_requirements)
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
    graph.add_edge("requirements", "approve_requirements")
    graph.add_conditional_edges("approve_requirements", route_requirements)
    graph.add_edge("implementation", "approve_implementation")
    graph.add_conditional_edges("approve_implementation", route_implementation)
    graph.add_edge("acceptance_tests", "approve_acceptance_tests")
    graph.add_conditional_edges("approve_acceptance_tests", route_acceptance_tests)
    graph.add_edge("unit_tests", "approve_unit_tests")
    graph.add_conditional_edges("approve_unit_tests", route_unit_tests)

    return graph.compile()