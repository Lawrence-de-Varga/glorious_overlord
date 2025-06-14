from pathlib import Path
from decorators import type_check_decorator
from checking import extant_dir, extant_file


@type_check_decorator([Path | str, Path | str])
def get_file_content(working_directory, file_path):
    wd_path = Path(working_directory).resolve()
    exd = extant_dir(wd_path)
    # check if path exists and points to a dir
    if not isinstance(exd, bool):
        return exd

    f_path = Path(wd_path / file_path).resolve()
    # check if path exists and points to a file
    exf = extant_file(f_path)
    if not isinstance(exf, bool):
        return exf

    # check that file is within working directory
    try:
        f_path.relative_to(wd_path)
    except ValueError:
        return f'Error: Cannot read "{f_path}" as it is outside the permitted working directory'

    # collect file content into string.
    # Truncate if too large
    content_string = ""
    try:
        with f_path.open() as f:
            content_string += f.read()

        if len(content_string) > 10000:
            content_string = content_string[:10000]
            content_string += '[...File "{file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f"Error reading file: {f_path} content - {e}"

    return content_string
