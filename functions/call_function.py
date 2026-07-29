from google import genai
from collections.abc import Callable
from .get_file_content import get_file_content
from .get_files_info import get_files_info
from .run_python_file import run_python_file
from .write_file import write_file

def call_function(function_call, verbose: bool = False) -> dict:
    # get details of function from interaction step
    function_name = function_call.name
    function_args = function_call.arguments

    if verbose:
        print(f" - Calling function {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")
    
    function_map: dict[str: Callable[..., str]] = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file
    }

    # test if function call is valid and return if not
    if function_name not in function_map.keys():
        return {
        "type": "function_result",
        "name": function_name,
        "call_id": function_call.id,
        "result": [{"type": "text", 
                    "text": f"Error: Unknown function: {function_name}"}]
        }

    # set working directory
    function_args["working_directory"] = "./calculator"

    result = function_map[function_name](**function_args)
    return {
        "type": "function_result",
        "name": function_name,
        "call_id": function_call.id,
        "result": [{"type": "text", 
                    "text": result}]
        }