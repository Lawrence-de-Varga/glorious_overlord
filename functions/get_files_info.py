from pathlib import Path


def get_files_info(working_directory: str, directory=None) -> str:
    w_dir = Path(working_directory).resolve()

    print(w_dir.resolve())
    if not w_dir.exists():
        # print("does not exist")
        return f"Error: {w_dir} does not exist on this machine."

    if directory:
        directory_path = Path(w_dir / directory).resolve()
        print(directory_path)

    if not directory_path.exists():
        # print("does not exist")
        return f"Error: {directory_path} does not exist on this machine."

    if directory_path not in w_dir.iterdir() and directory_path != w_dir:
        # print("not in dir")
        return f'Error: Cannot list "{directory_path}" as it is outside the permitted working directory_path'

    if not directory_path.is_dir():
        # print("not dir")
        return f'Error: "{directory}" is not a directory'

    contents_info = ""
    for obj in directory_path.iterdir():
        contents_info += f"- {obj.name}: file_size={obj.stat().st_size} bytes, is_dir={obj.is_dir()}\n"

    return contents_info


# get_files_info(Path.cwd(), Path(Path.cwd() / "calculator"))
