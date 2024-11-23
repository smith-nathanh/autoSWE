from typing import Any, List, Dict, Type, Union, Literal, Annotated
from langchain_core.tools import tool
from langgraph.prebuilt import InjectedState, ToolNode, ToolExecutor, tools_condition
from system.structure import GraphState

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


@tool
def bash(command: str, state: Annotated[dict, InjectedState]) -> str:
    """
   "Run commands in a bash shell\n
    * When invoking this tool, the contents of the \"command\" parameter does NOT need to be XML-escaped.\n
    * You don't have access to the internet via this tool.\n
    * You do have access to a mirror of common linux and python packages via apt and pip.\n
    * State is persistent across command calls and discussions with the user.\n
    * To inspect a particular line range of a file, e.g. lines 10-25, try 'sed -n 10,25p /path/to/the/file'.\n
    * Please avoid commands that may produce a very large amount of output.\n
    * Please run long lived commands in the background, e.g. 'sleep 10 &' or start a server in the background.",
    """
    import subprocess
    try:
        output = subprocess.check_output(command, shell=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output

# This is from https://www.anthropic.com/research/swe-bench-sonnet 
# {
#    "name": "bash",
#    "description": "Run commands in a bash shell\n
# * When invoking this tool, the contents of the \"command\" parameter does NOT need to be XML-escaped.\n
# * You don't have access to the internet via this tool.\n
# * You do have access to a mirror of common linux and python packages via apt and pip.\n
# * State is persistent across command calls and discussions with the user.\n
# * To inspect a particular line range of a file, e.g. lines 10-25, try 'sed -n 10,25p /path/to/the/file'.\n
# * Please avoid commands that may produce a very large amount of output.\n
# * Please run long lived commands in the background, e.g. 'sleep 10 &' or start a server in the background.",
#    "input_schema": {
#        "type": "object",
#        "properties": {
#            "command": {
#                "type": "string",
#                "description": "The bash command to run."
#            }
#        },
#        "required": ["command"]
#    }
# }