import json
import shutil
from pathlib import Path

PATH_START = "D:/MCP/asset/"  

def get_folder_file_structure(directory_path=PATH_START):
    """
    Returns folders (with /) and files as separate lists.
    """
    directory_path = Path(directory_path)

    if not directory_path.exists() or not directory_path.is_dir():
        raise ValueError(f"{directory_path} is not a valid directory.")

    folders = []
    files = []

    for path in directory_path.rglob("*"):
        rel_path = path.relative_to(directory_path).as_posix()
        if path.is_dir():
            folders.append(rel_path + "/")
        else:
            files.append(rel_path)

    return json.dumps({"folders": sorted(folders), "files": sorted(files)})

def move_file(src, dest):
    """
    Moves a file from src to dest.
    Creates destination folders if they don't exist.
    
    Parameters:
        src (str or Path): Source file path.
        dest (str or Path): Destination file path.
    """
    src_path = Path(PATH_START) / src
    dest_path = Path(PATH_START) / dest

    if not src_path.exists() or not src_path.is_file():
        raise FileNotFoundError(f"Source file '{src}' does not exist.")
    
    if not dest_path.parent.exists():
        raise FileNotFoundError(f"Destination folder '{dest}' does not exist.")

    shutil.move(str(src_path), str(dest_path))
    return json.dumps({"message": f"Moved '{src}' -> '{dest}'"})

def read_txt_file(src):
    """
    Reads a .txt file from the given relative path.

    Parameters:
        src (str or Path): Relative path to the text file (e.g., "folder1/test1.txt").

    Returns:
        str: JSON string containing:
            - "message": A description of the read operation.
            - "content": The file contents as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not a .txt file.
    """
    src_path = Path(PATH_START) / src

    # Check if file exists
    if not src_path.exists() or not src_path.is_file():
        raise FileNotFoundError(f"Source file '{src}' does not exist.")

    # Check extension is .txt
    if src_path.suffix.lower() != ".txt":
        raise ValueError(f"File '{src}' is not a .txt file.")

    # Read the file content
    content = src_path.read_text(encoding="utf-8-sig")

    # Return JSON with relative path and content
    return json.dumps({
        "message": f"Read '{src_path.relative_to(PATH_START).as_posix()}'",
        "content": content
    }, ensure_ascii=False)

if __name__ == "__main__":

    contents = get_folder_file_structure()
    print(contents)
    # print("Folders:", contents["folders"])
    # print("Files:", contents["files"])

    # res = move_file("folder1/test1.txt", "folder2/test1.txt")
    # res = move_file("folder2/test1.txt", "folder1/test1.txt")
    # print(res)

    res = read_txt_file("folder1/test1.txt")
    print(res)


