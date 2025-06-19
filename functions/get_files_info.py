import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    abspath = os.path.abspath(working_directory)
    if directory != None:
        directory_abspath = os.path.abspath(os.path.join(working_directory, directory)) + os.sep
        working_directory_abspath = os.path.abspath(working_directory) + os.sep
        abspath = os.path.abspath(os.path.join(working_directory, directory))
        if not directory_abspath.startswith(working_directory_abspath):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory_abspath):
        return f'Error: "{directory}" is not a directory'
    items = os.listdir(directory_abspath)
    output = ""
    for item in items:
        try:
            item_path = os.path.join(directory_abspath, item)
            output += " - " + item + ": "
            output += f"file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}\n"
        except Exception as e:
            return  f'Error: item {item} not found'

    return output

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
