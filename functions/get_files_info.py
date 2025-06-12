import os

def get_files_info(working_directory, directory = None):
    try:
        if directory == "." or directory is None:
            directory = working_directory
        absolute_working_dir = os.path.abspath(working_directory)
        working_dir_list = os.listdir(absolute_working_dir)
        
        if not (directory in working_dir_list or directory == working_directory):
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
        target_dir = absolute_working_dir
        if directory != working_directory:
            target_dir = os.path.join(target_dir, directory)
        if not os.path.isdir(target_dir):
            return f"Error: \"{directory}\" is not a directory"
        
        target_dir_files = os.listdir(target_dir)
        file_data = []
        for file in target_dir_files:
            path_to_file = os.path.join(target_dir, file)
            is_dir = True
            if os.path.isfile(path_to_file):
                is_dir = False
            file_size = os.path.getsize(path_to_file)
            file_data_string = f"- {file}: file_size={file_size} bytes, is_dir={is_dir}"
            file_data.append(file_data_string)
        file_data_string = "\n".join(file_data)
        return file_data_string
    except Exception as e:
        return f"Error: {e}"