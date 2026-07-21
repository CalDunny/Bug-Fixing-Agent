import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    # return errors as strings for Gemini to proccess
    try:
        # validate file path
        working_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_abs, file_path))
    
        valid_file = os.path.commonpath([working_abs, target_file]) == working_abs
    
        if not valid_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # read file contents
        with open(target_file, "r") as f:
            contents = f.read(MAX_CHARS)
        # check if content was cut off
            if f.read(1):
                contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return contents
    
    except Exception as e:
        return f"Error: {e}"