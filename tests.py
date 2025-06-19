from functions.get_file_content import get_file_content

def test():
    print("Testing get_file_content: --- working_directory, file_path ---")
    print(" --- calculator, main.py ---")
    print(get_file_content("calculator", "main.py"))
    print(" --- calculator, pkg/calculator.py ---")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(" --- calculator, /bin/cat ---")
    print(get_file_content("calculator", "/bin/cat"))

if  __name__ == "__main__":
    test()
