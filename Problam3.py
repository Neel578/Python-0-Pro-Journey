import os

def print_files_only(path):
    try:
        entries = os.listdir(path)
    except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
        print("Error:", e)
        return

    print(f"Files in '{path}':")
    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path):  # only print if it is a file
            print(entry)

if __name__ == "__main__":
    dir_path = "."
    print_files_only(dir_path)
