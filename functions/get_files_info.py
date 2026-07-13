
import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    # Check directoy is valid and within working_directory
    # Return strings for Gemini to proccess
    try:
        working_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_abs, directory))
    
        valid_dir = os.path.commonpath([working_abs, target_dir]) == working_abs
    except Exception as e:
        return f"Error: {e}"
    
    if not valid_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    return f'Success: "{directory}" is within the working directory'