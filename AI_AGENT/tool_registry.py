from google.genai import types
from linux_tools import get_disk_usage


TOOLS = {
    "get_disk_usage": get_disk_usage
}


get_disk_usage_declaration = types.FunctionDeclaration(
    name="get_disk_usage",
    description="Gets the current disk usage of the Linux system.",
    parameters_json_schema={
        "type": "object",
        "properties": {}
    }
)


TOOL_DEFINITIONS = [
    types.Tool(
        function_declarations=[get_disk_usage_declaration]
    )
]
