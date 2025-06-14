from pathlib import Path
from decorators import type_check_decorator
from checking import extant_dir, extant_file
import subprocess
import sys


@type_check_decorator([Path | str, Path | str])
def run_python_file(working_directory, file_path):
    wd_path = Path(working_directory).resolve()

    # Check that wd_path exists and is a dir
    exd = extant_dir(wd_path)
    if not isinstance(exd, bool):
        return exd

    f_path = Path(wd_path / file_path).resolve()
    # Check that it is a python file
    if f_path.suffix != ".py":
        return f'Error: "{f_path}" is not a Python file.'

    # Check that f_path is in wd_path
    try:
        f_path.relative_to(wd_path)
    except ValueError:
        return f'Error: Cannot read "{f_path}" as it is outside the permitted working directory'

    # Check that f_path exists and points to a file
    exf = extant_file(f_path)
    if not isinstance(exf, bool):
        return exf

    # Attempt to run the give file. 15 second timeout.
    try:
        result = subprocess.run(["/usr/bin/python", f_path], timeout=15, check=True)
    except subprocess.CalledProcessError as e:
        return f"Process exited with code: {e.returncode}"

    print(result.stdout)
    print(result.stderr)
    doutderr = []
    if not result.stdout:
        doutderr.append("No stdout was produced.")
    else:
        doutderr.append("STDOUT:" + result.stdout)

    if not result.stderr:
        doutderr.append("No stderr was produced.")
    else:
        doutderr.append("STDEER:" + result.stderr)

    return doutderr


print(run_python_file("../calculator", "main.py"))
print()
print(run_python_file("../calculator", "tests.py"))
print()
print(run_python_file("../calculator", "../../cheese.py"))
print()
print(run_python_file("../calculator", "nonexistent.py"))
print()
