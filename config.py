from functions.schemas import (schema_get_files_info, schema_write_file, 
                               schema_run_python_file, schema_get_file_content)

MAX_CHARS = 10000
TIMEOUT = 30.00
PY_EXT = ".py"
CALL_LIMIT = 20

SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

AVAILABLE_FUNCTIONS = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file
]
