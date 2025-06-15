import os, subprocess

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
        result = subprocess.run(["python3", target_file_path], timeout = 30, capture_output = True) 
        result_string = f"STDOUT: {result.stdout}"
        result_string += f"STDERR: {result.stderr}"
        if result.returncode != 0:
            result_string += f"Process exited with code {result.returncode}"
        return result_string
    except Exception as e:
        return f"Error: executing Python file: {e}"