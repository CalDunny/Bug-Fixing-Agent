
import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    # return errors as strings for Gemini to proccess
    try:
        # check directoy is valid and within working_directory
        working_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_abs, directory))
    
        valid_dir = os.path.commonpath([working_abs, target_dir]) == working_abs

        if not valid_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
    
        # list the info of the directory/file
        dir_items = os.listdir(target_dir)
        results = []
        for item in dir_items:
            item_path = os.path.join(target_dir, item)
            results.append((os.path.getsize(item_path), os.path.isdir(item_path)))

        output = ""
        for i in range(len(results)):
            output += f"- {dir_items[i]}: file_size={results[i][0]} bytes, is_dir={results[i][1]}\n"
        return output
    
    except Exception as e:
        return f"Error: {e}"
