import os
from google.genai import types

def get_files_info(working_directory, directory = None):
    absolute_working_dir = os.path.abspath(working_directory)
    target_dir = absolute_working_dir
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(absolute_working_dir):
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
    if not os.path.isdir(target_dir):
        return f"Error: \"{directory}\" is not a directory"
    try:    
        target_dir_files = os.listdir(target_dir)
        file_data = []
        for file in target_dir_files:
            path_to_file = os.path.join(target_dir, file)
            is_dir = os.path.isdir(path_to_file)
            file_size = os.path.getsize(path_to_file)
            file_data_string = f"- {file}: file_size={file_size} bytes, is_dir={is_dir}"
            file_data.append(file_data_string)
        file_data_string = "\n".join(file_data)
        return file_data_string
    except Exception as e:
        return f"Error listing files: {e}"
    
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