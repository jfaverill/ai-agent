import os

def write_file(working_directory, file_path, content):
    absolute_working_dir = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file_path.startswith(absolute_working_dir):
        return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"
    try:       
        with open(target_file_path, "w") as f:
            f.write(content)

        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error writing file {file_path}: {e}"
