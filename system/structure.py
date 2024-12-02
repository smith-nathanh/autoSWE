from typing import Any, List, Dict, Type, Union, Literal, Annotated
from typing_extensions import TypedDict
from pydantic import BaseModel, Field

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
    acceptance_tests: Dict[str, str] = Field(
        description="Dictionary containing acceptance test content and command",
        example={
            "test_features": "import unittest\n...",
            "command": "python -m unittest tests/acceptance/test_features.py"
        }
    )

class UnitTests(BaseModel):
    unit_tests: Dict[str, str] = Field(
        description="Dictionary containing test_module and command keys",
        example={
            "test_module": "import unittest\nclass TestExample(unittest.TestCase):\n    def test_something(self):\n        pass",
            "command": "python -m unittest tests/unit/test_module.py"
        }
    )

class UpdateDocument(BaseModel):
    content: str
