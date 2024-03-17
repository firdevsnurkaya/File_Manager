import os

def create_directory(directory_name):
    os.makedirs(directory_name, exist_ok=True)

def list_files(directory="."):
    return os.listdir(directory)

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("Dosya bulunamadı")

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
