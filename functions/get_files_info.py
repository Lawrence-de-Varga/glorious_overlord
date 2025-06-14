from pathlib import Path

from checking import extant_dir

from decorators import type_check_decorator


@type_check_decorator([Path | str, Path | str | None])
def get_files_info(working_directory, directory=None) -> str:
    """
    Lists all files and directories in directory if directory is
    within working directory.
    Currently does not account for a working directory
    with the same name as the directory, e.g /src/src.
    Returns error strings for an llm to ingest.
    """

    wd_path = Path(working_directory).resolve()
    exd = extant_dir(wd_path)
    # Check if wd_path exists and is a directory
    # if not return an error string provided by extant_dir
    if not isinstance(exd, bool):
        return exd

    if directory:
        d_path = Path(wd_path / directory).resolve()
    else:
        return f"Error: {directory} is None or false."

    # Check if d_path exists and is a directory
    # return error string if not
    exd = extant_dir(d_path)
    if not isinstance(exd, bool):
        return exd

    try:
        d_path.relative_to(wd_path)
    except ValueError:
        return f'Error: Cannot list "{d_path}" \nas it is outside the permitted working directory: {wd_path}'

    contents_info = ""
    try:
        for obj in d_path.iterdir():
            contents_info += f"- {obj.name}: file_size={obj.stat().st_size} bytes, is_dir={obj.is_dir()}\n"
    except Exception as e:
        return f"Error listing files: {e}"

    return contents_info


print(get_files_info("../calculator", "../"))
