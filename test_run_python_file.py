from functions.run_python_file import run_python_file

def test_run_python_file(working_dir: str, file_path: str, args: list[str] | None=None):
    print(f"Calling: get_file_content('{working_dir}', '{file_path}', '{args}')")
    result = run_python_file(working_dir, file_path, args)

    print(f"Returned:\n{result}\n")

test_run_python_file("calculator", "main.py")
test_run_python_file("calculator", "main.py", ["3 + 5"])
test_run_python_file("calculator", "tests.py")
test_run_python_file("calculator", "../main.py")        # should return error
test_run_python_file("calculator", "nonexistent.py")    # should return error
test_run_python_file("calculator", "lorem.txt")         # should return error
