from pathlib import Path
from decorators import type_check_decorator


@type_check_decorator([Path | str, Path | str])
def get_file_content(working_directory, file_path):
    w_dir = Path(working_directory).resolve()
    # print(w_dir)
    if not w_dir.exists():
        # print("w_dir does not exist.")
        return f"Error: {w_dir} does not exist."

    if not w_dir.is_dir():
        # print("w_dir is not a dir.")
        return f"Error: {w_dir} is not a directory."

    f_path = Path(w_dir / file_path).resolve()
    # print(f_path)

    if not f_path.exists():
        # print("f_path does not exist.")
        return f"Error: {f_path} does not exist."

    if not f_path.is_file():
        # print("f_path is not a file.")
        return f'Error: File not found or is not a regular file: "{f_path}"'

    try:
        f_path.relative_to(w_dir)
    except ValueError:
        return f'Error: Cannot read "{f_path}" as it is outside the permitted working directory'

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


# print(get_file_content(Path.cwd(), "345"))
