
schema_get_file_content: dict = {
    "type": "function",
    "name": "get_file_content",
    "description": "Lists the contents of a specified file within the working directory up to a maximum of the first 10000 characters.",
    "parameters": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "File path to list contnets from, relative to the working directory.",
            }
        },
        "required": ["file_path"]
    }
}

schema_get_files_info: dict = {
    "type": "function",
    "name": "get_files_info",
    "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
    "parameters": {
        "type": "object",
        "properties": {
            "directory": {
                "type": "string",
                "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
            }
        }
    }
}

schema_run_python_file: dict = {
    "type": "function",
    "name": "run_python_file",
    "description": "Runs the given Python file and returns the stdout and stderr from the process.",
    "parameters": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "File path to run, relative to the working directory and must be a Python file.",
            },
            "args": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Arguments to pass to the Python program.",
            }
        },
        "required": ["file_path"]
    }
}

schema_write_file: dict = {
    "type": "function",
    "name": "write_file",
    "description": "Writes content to the provided file, replacing any content it previously contained.",
    "parameters": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "File path to write to, relative to the working directory.",
            },
            "content": {
                "type": "string",
                "description": "Content to be written into the file.",
            }
        },
        "required": ["file_path", "content"]
    }
}