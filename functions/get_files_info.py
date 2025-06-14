from pathlib import Path
from decorators import type_check_decorator


@type_check_decorator([Path | str, str | Path | None])
def get_files_info(working_directory: str, directory=None) -> str:
    w_dir = Path(working_directory).resolve()

    print(w_dir.resolve())
    if not w_dir.exists():
        # print("does not exist")
        return f"Error: {w_dir} does not exist on this machine."

    if directory:
        directory_path = Path(w_dir / directory).resolve()
        print(directory_path)
    else:
        return f"Error: {directory} is None or false."

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
    try:
        for obj in directory_path.iterdir():
            contents_info += f"- {obj.name}: file_size={obj.stat().st_size} bytes, is_dir={obj.is_dir()}\n"
    except Exception as e:
        return f"Error listting files: {e}"

    return contents_info


# print(get_files_info(345, True))
