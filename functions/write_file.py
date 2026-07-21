import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    # return errors as strings for Gemini to proccess
    try:
        # validate file path
        working_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_abs, file_path))
    
        valid_dir = os.path.commonpath([working_abs, target_file]) == working_abs
    
        if not valid_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
    

        # make sure parent directories exist
        os.makedirs(file_path, exist_ok=True)
        # write new contents to file
        with open(target_file, "w") as f:
            f.write(content)
   
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {e}"