import os
from config import MAX_CHARS
from google.genai import types

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

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the content of the file at the given file path within the working directory  ",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to read from",
            ),
        },
    ),
)
