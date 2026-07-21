from functions.get_files_info import get_files_info

def test_get_files_info(working_dir: str, directory: str):
    print(f"Calling: get_files_info('{working_dir}', '{directory}')")
    result = get_files_info(working_dir, directory)
    if directory==".": directory="current"
    print(f"Result for '{directory}' directory:\n{result}\n")

test_get_files_info("calculator", ".")
test_get_files_info("calculator", "pkg")
test_get_files_info("calculator", "/bin")       # should error
test_get_files_info("calculator", "../")        # should error