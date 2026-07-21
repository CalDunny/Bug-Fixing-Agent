from functions.get_file_content import get_file_content

def test_get_file_content(working_dir: str, file_path: str):
    print(f"Calling: get_file_content('{working_dir}', '{file_path}')")
    result = get_file_content(working_dir, file_path)

    print(f"Contents of {file_path}:\n{result}\n")

# lorem ipsum test
content = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(content)}")
print(f"lorem.txt truncated: {'truncated' in content}")

test_get_file_content("calculator", "main.py")
test_get_file_content("calculator", "pkg/calculator.py")
test_get_file_content("calculator", "/bin/cat")     # should error
test_get_file_content("calculator", "pkg/does_not_exist.py")    # should error
