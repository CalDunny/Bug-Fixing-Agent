from functions.write_file import write_file

def test_write_file(working_dir: str, file_path: str, content: str):
    print(f"Calling: get_file_content('{working_dir}', '{file_path}', '{content}')")
    result = write_file(working_dir, file_path, content)

    print(f"Returned:\n{result}\n")

test_write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
test_write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
test_write_file("calculator", "/tmp/temp.txt", "this should not be allowed")    #should error

