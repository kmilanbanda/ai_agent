import os

def write_file(working_directory, file_path, content):
    file_abspath = os.path.abspath(os.path.join(working_directory, file_path))
    working_directory_abspath = os.path.abspath(working_directory)
    if not file_abspath.startswith(working_directory_abspath + os.sep):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_abspath):
        try:
            os.makedirs(os.path.dirname(file_abspath), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(file_abspath) and os.path.isdir(file_abspath):
        return f'Error: "{file_path}" is a dirrectory, not a file'
    try:
        with open(file_abspath, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: writing to file: {e}"

