from pathlib import Path
from decorators import type_check_decorator
from checking import extant_dir, extant_file, exists


@type_check_decorator([str | Path, str | Path, str])
def write_file(working_directory, file_path, content):
    """
    Takes a path to a directory and path to a file
    and a string of content to be written.
    Ensures that the directory exists.
    Ensures that the file is within the specified directory
    and overwrites it if it exists.
    If it does not exist, it ensures that the path is
    within the specified directory and creates and writes to it.
    """

    wd_path = Path(working_directory).resolve()

    # check if given directory path exists and is a directory.
    exd = extant_dir(wd_path)
    if not isinstance(exd, bool):
        return exd

    # resolve file path and check that it is within the working directory
    f_path = Path(wd_path / file_path).resolve()
    try:
        f_path.relative_to(wd_path)
    except ValueError:
        return f'Error: Cannot read "{f_path}" as it is outside the permitted working directory: {wd_path}'

    exf = extant_file(f_path)
    try:
        # if it exists and is a file, overwrite it
        if isinstance(exf, bool):
            f_path.write_text(content)
            return (
                f'Successfully wrote to "{f_path}" ({len(content)} characters written)'
            )
        ef = exists(f_path)
        # if it does not exist, create it and write to it.
        if not isinstance(ef, bool):
            f_path.touch()
            f_path.write_text(content)
            return (
                f'Successfully wrote to "{f_path}" ({len(content)} characters written)'
            )
        else:
            # if we hit this its a directory
            return exf

    except Exception as e:
        return f"Error: failed to create or write to {f_path} with error: {e}"
