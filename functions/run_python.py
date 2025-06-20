import os, subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    absolute_working_dir = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file_path.startswith(absolute_working_dir):
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"
    if not os.path.exists(target_file_path):
        return f"Error: File \"{file_path}\" not found."
    if not target_file_path.endswith(".py"):
        return f"Error: \"{file_path}\" is not a Python file."
    try:
        result = subprocess.run(["python", target_file_path], timeout = 30, capture_output = True,
                                text = True) 
        result_string = f"STDOUT: {result.stdout}"
        result_string += f"STDERR: {result.stderr}"
        if result.returncode != 0:
            result_string += f"Process exited with code {result.returncode}"
        return result_string
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_get_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in a specified file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path pointing to the file to be executed, relative to the working directory.",
            ),
        },
    ),
)