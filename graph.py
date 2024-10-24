from typing import Any, List, Dict, Type, Union
from typing_extensions import TypedDict
from langchain.schema import Document
from langgraph.graph import StateGraph, START, END
from prompts import *
from langchain_core.messages import HumanMessage
import logging


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        prompt: prompt
        documents: dictionary of documents
    """
    prompt: str
    passed: Dict[str, bool]
    code: str
    tests_acceptance: str
    test_unit: str
    documents: Dict[str, Document]

def software_design(state: GraphState):
    """
    Designs the markdown files for the software design.
    """
    logging.info("---SOFTWARE DESIGN---")
    design_prompt = DESIGN_PROMPT.format(prd=state["documents"]["PRD"].content)
    #documents = llm.invoke([HumanMessage(content=design_prompt)]) # use structured outputs here
    documents = {"PRD": state["documents"]["PRD"].content,
                 "UML_class": Document("UML class diagram using mermaid syntax"),
                 "UML_sequence": Document("UML sequence diagram using mermaid syntax"),
                 "architecture_design": Document("Architecture design as a text based representation of the file tree")}
    return {"documents": documents}

def design_review(state: GraphState):
    """
    LLM-as-a-judge to review the design documents.
    """
    logging.info("---REVIEWING DESIGN DOCUMENTS---")
    prompt = DESIGN_PROMPT.format(prd=state["documents"]["PRD.md"].content)
    #passed = llm.invoke([HumanMessage(content=prompt)]) # use structured outputs here
    passed = {"UML_class": True, "UML_sequence": True, "architecture_design": True}
    return {"documents": state["documents"],
            "passed": passed}

def determine_requirements(state: GraphState):
    """
    Based on the design documents, determine the requirements.txt file.
    """
    logging.info("---DETERMINING REQUIREMENTS---")
    prompt = REQUIREMENTS_PROMPT.format(prd=state["documents"]["PRD"].content,
                                        UML_class=state["documents"]["UML_class"].content,
                                        UML_sequence=state["documents"]["UML_sequence"].content,
                                        architecture_design=state["documents"]["architecture_design"].content)
    requirements = llm.invoke([HumanMessage(content=prompt)]) # use structured outputs here
    state["documents"].update(requirements)
    return state

def test_requirements(state: GraphState):
    """
    Test the requirements.txt file.
    """
    logging.info("---TESTING REQUIREMENTS---")
    # need a shell to run the requirements.txt file and see if it works
    state['passed'].update({"requirements": True})
    return state

def implementation(state: GraphState):
    """
    Implement the software design.
    """
    logging.info("---IMPLEMENTING SOFTWARE DESIGN---")
    prompt = IMPLEMENTATION_PROMPT.format(prd=state["documents"]["PRD.md"].content,
                                          UML_class=state["documents"]["UML_class"].content,
                                          UML_sequence=state["documents"]["UML_sequence"].content,
                                          architecture_design=state["documents"]["architecture_design"].content,
                                          requirements=state["documents"]["requirements"].content)
    state["code"] = llm.invoke([HumanMessage(content=prompt)]) # use structured outputs here
    return state

def acceptance_tests(state: GraphState):
    """
    Generate acceptance tests for the software.
    """
    logging.info("---GENERATING ACCEPTANCE TESTS---")
    prompt = ACCEPTANCE_TEST_PROMPT.format(prd=state["documents"]["PRD.md"].content,
                                           UML_class=state["documents"]["UML_class"].content,
                                           UML_sequence=state["documents"]["UML_sequence"].content,
                                           architecture_design=state["documents"]["architecture_design"].content)
    tests = llm.invoke([HumanMessage(content=prompt)]) # use structured outputs here
    state["tests_acceptance"] = tests
    return state

def unit_tests(state: GraphState):
    """
    Generate unit tests for the software.
    """
    logging.info("---GENERATING UNIT TESTS---")
    prompt = UNIT_TEST_PROMPT.format(prd=state["documents"]["PRD.md"].content,
                                     UML_class=state["documents"]["UML_class"].content,
                                     UML_sequence=state["documents"]["UML_sequence"].content,
                                     architecture_design=state["documents"]["architecture_design"].content,
                                     requirements=state["documents"]["requirements"].content)
    tests = llm.invoke([HumanMessage(content=prompt)]) # use structured outputs here
    state["tests_unit"] = tests
    return state


def build_graph():
    graph_builder = StateGraph(GraphState)

    # nodes
    graph_builder.add_node("software_design", software_design)
    graph_builder.add_node("design_review", design_review)
    graph_builder.add_node("determine_requirements", determine_requirements)
    graph_builder.add_node("test_requirements", test_requirements)
    graph_builder.add_node("implementation", implementation)
    graph_builder.add_node("acceptance_tests", acceptance_tests)
    graph_builder.add_node("unit_tests", unit_tests)

    # edges
    graph_builder.add_edge(START, "software_design")
    graph_builder.add_edge("software_design", "design_review")
    graph_builder.add_edge("design_review", "determine_requirements")
    graph_builder.add_edge("determine_requirements", "test_requirements")
    graph_builder.add_edge("test_requirements", "implementation")
    graph_builder.add_edge("implementation", "acceptance_tests")
    graph_builder.add_edge("acceptance_tests", "unit_tests")
    graph_builder.add_edge("unit_tests", END)

    return graph_builder.compile()