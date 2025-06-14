from pathlib import Path
from decorators import type_check_decorator


@type_check_decorator([Path])
def dir_check(obj):
    if obj.is_dir():
        return True
    return f"Error: {obj} is not a directory."


@type_check_decorator([Path])
def file_check(obj):
    if obj.is_file():
        return True
    return f"Error: {obj} is not a file."


@type_check_decorator([Path])
def exists(obj):
    if obj.exists():
        return True
    return f"Error: {obj} does not exist."


@type_check_decorator([Path])
def extant_file(obj):
    try:
        e = exists(obj)
        f = file_check(obj)

        if not isinstance(e, bool):
            return e
        if not isinstance(f, bool):
            return f
        return True
    except Exception as e:
        return f"Error: extant_file failed with error: {e}"


@type_check_decorator([Path])
def extant_dir(obj):
    try:
        e = exists(obj)
        d = dir_check(obj)

        if not isinstance(e, bool):
            return e
        if not isinstance(d, bool):
            return d
        return True
    except Exception as e:
        return f"Error: extant_dir failed with error: {e}"
