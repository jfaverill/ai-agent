import os

def get_file_content(working_directory, file_path):
    try:
        absolute_working_dir = os.path.abspath(working_directory)
        target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not target_file_path.startswith(absolute_working_dir):
            return f"Error: Cannot read \"{target_file_path}\" as it is outside the permitted working directory"
        if not os.path.isfile(target_file_path):
            return f"Error: File not found or is not a regular file: \"{target_file_path}\""
        
        MAX_CHARS = 10000
        max_chars_exceeded = False
        with open(target_file_path, "r") as f:
            file_content_string = f.read()

        max_chars_exceeded = len(file_content_string) > MAX_CHARS
        if max_chars_exceeded:
            file_content_string = f"{file_content_string[:MAX_CHARS]}[...File \"{target_file_path}\" truncated at 10000 characters]"
        return file_content_string
    except Exception as e:
        return f"Error: {e}"
