import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    working_directory_abspath = os.path.abspath(working_directory)
    file_abspath = os.path.abspath(os.path.join(working_directory, file_path))
    if not file_abspath.startswith(working_directory_abspath):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_abspath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(file_abspath, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) == 10000:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]' 
        return file_content_string 
