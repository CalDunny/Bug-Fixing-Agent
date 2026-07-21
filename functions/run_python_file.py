import os
import subprocess
from config import PY_EXT, TIMEOUT

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    # return errors as strings for Gemini to proccess
    try:
        # check file is valid and within working_directory
        working_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_abs, file_path))
    
        valid_dir = os.path.commonpath([working_abs, target_file]) == working_abs
    
        
        if not valid_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if file_path[-3:] != PY_EXT:
            return f'Error: "{file_path}" is not a Python file'
        
        # run file using subprocesses
        command = ["python", target_file]
        if args is not None: command.extend(args)

        cmplt_process = subprocess.run(command, cwd=working_abs, text=True, timeout=TIMEOUT,
                                       capture_output=True)
        process_output = cmplt_process.stdout
        process_error = cmplt_process.stderr
        
        output = ""
        if cmplt_process.returncode != 0:
            output += f"Process exited with code {cmplt_process.returncode}\n"
        
        if not (process_output or process_error):
            output += "No output produced"
        else:
            output += f"STDOUT: {process_output}\n"
            output += f"STDERR: {process_error}"
        
        return output

    except Exception as e:
            return f"Error: executing Python file: {e}"