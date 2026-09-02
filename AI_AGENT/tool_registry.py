
from google.genai import types

from linux_tools import (
    get_disk_usage,
    get_processes
)


TOOLS = {
    "get_disk_usage": get_disk_usage,
    "get_processes": get_processes
}


get_disk_usage_declaration = types.FunctionDeclaration(
    name="get_disk_usage",
    description="Gets the current disk usage of the Linux system.",
    parameters_json_schema={
        "type": "object",
        "properties": {}
    }
)


get_processes_declaration = types.FunctionDeclaration(
    name="get_processes",
    description="Gets running Linux processes sorted by CPU or memory usage.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "sort_by": {
                "type": "string",
                "description": "Sort processes by CPU or memory usage.",
                "enum": ["cpu", "memory"]
            }
        },
        "required": ["sort_by"]
    }
)


TOOL_DEFINITIONS = [
    types.Tool(
        function_declarations=[
            get_disk_usage_declaration,
            get_processes_declaration
        ]
    )
]

