from functions.write_file import write_file
from functions.get_file_content import get_file_content
from functions.run_python import run_python_file

def test():
    #print("Testing get_file_content: --- working_directory, file_path ---")
    #print(" --- calculator, main.py ---")
    #print(get_file_content("calculator", "main.py"))
    #print(" --- calculator, pkg/calculator.py ---")
    #print(get_file_content("calculator", "pkg/calculator.py"))
    #print(" --- calculator, /bin/cat ---")
    #print(get_file_content("calculator", "/bin/cat"))

    #print("Testing write_file: ")
    #print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    #print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    #print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))

if  __name__ == "__main__":
    test()
    
