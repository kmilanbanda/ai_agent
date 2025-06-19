import os
from subprocess import run

def run_python_file(working_directory, file_path):
    working_directory_abspath = os.path.abspath(working_directory)
    file_abspath = os.path.abspath(os.path.join(working_directory, file_path))
    if not file_abspath.startswith(working_directory_abspath + os.sep):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_abspath):
        return f'Error: File "{file_path}" not found.'
    if not file_abspath.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = run(["python", file_abspath], capture_output=True, cwd=working_directory_abspath, timeout=30, text=True)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    if len(completed_process.stdout) == 0 and len(completed_process.stderr) == 0:
        return "No output produced"
    output = f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}\n"
    if completed_process.returncode != 0:
        output += "Process exited with code {completed_process.returncode}"
    return output
