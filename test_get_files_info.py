from functions.get_files_info import get_files_info

def test_get_files_info(working_dir: str, directory: str):
    print(f'Calling: get_files_info("{working_dir}", "{directory}")')
    result = get_files_info(working_dir, directory)
    print(f'Result: {result}\n')

test_get_files_info("calculator", ".")
test_get_files_info("calculator", "/bin")
test_get_files_info("calculator", "../")
test_get_files_info("calculator", "main.py")