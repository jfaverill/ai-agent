import os
from google.genai import types

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
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes specified content out to a file in a specified file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path pointing to the file to be written to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the target file at the end of the specified file path.",
            ),
        },
        required=["file_path", "content"],
    ),
)
