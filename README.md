# python-pre-commit-linter-tutorial

## How to
1. Make sure you have the `.pre-commit-config.yaml` with the respective content. You can refer into the file on this repo.
2. Install requirements
```bash
pip3 install -r requirements.txt
```
3. Install pre-commit hooks in your machine
```bash
pre-commit install
```
4. Try add the codes with your own
5. For example the initial codes
```python
from pydantic import BaseModel

from typing import Union

from fastapi import FastAPI


class Employee(BaseModel):
    name: str
    description: Union[str, None] = None
    salary: float
    tax: Union[float, None] = None
app = FastAPI()
@app.put("/employees/{employee_id}")
async def create_employee(employee_id: int, employee: Employee, description: Union[str, None] = None):
    result = {"employee_id": employee_id, **employee.dict()}
    if description:
        result.update({"description": description})
    return result
```
6. Add into git `git add .`
7. Commit into git `git commit -m "chore: demo purpose"`
8. Then you will see the following output that indicate installing the library which already defined in `.pre-commit-config.yaml`. Later on, you wouldn't see this message in the future commit because it is already installed
```bash
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /Users/fajarmuslim/.cache/pre-commit/patch1664279121-8623.
[INFO] Installing environment for https://github.com/asottile/seed-isort-config.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://github.com/ambv/black.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://gitlab.com/pycqa/flake8.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
```
9. The another output as follows:
```bash
seed isort known_third_party.............................................Failed
- hook id: seed-isort-config
- exit code: 1

Creating an .isort.cfg with a known_third_party setting. Feel free to move the setting to a different config file in one of .editorconfig, .isort.cfg, setup.cfg, tox.ini, pyproject.toml.

This setting should be committed.

isort (python)...........................................................Failed
- hook id: isort
- files were modified by this hook

Fixing /Users/fajarmuslim/Documents/python-pre-commit-linter-tutorial/main.py

black....................................................................Failed
- hook id: black
- files were modified by this hook

reformatted main.py

All done! ✨ 🍰 ✨
1 file reformatted.

flake8...................................................................Passed
[INFO] Restored changes from /Users/fajarmuslim/.cache/pre-commit/patch1664279121-8623.
```
The above output indicate, that the first run will create the .isort.cfg file to save the import sort generated config. Then the isort modify the files related to sorting import. The piece of code that refactored as follows
```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
```

Black modify the codes to
```python
class Employee(BaseModel):
    name: str
    description: Union[str, None] = None
    salary: float
    tax: Union[float, None] = None


app = FastAPI()


@app.put("/employees/{employee_id}")
async def create_employee(
    employee_id: int, employee: Employee, description: Union[str, None] = None
):
    result = {"employee_id": employee_id, **employee.dict()}
    if description:
        result.update({"description": description})
    return result
```

Then the flake8 will lint our codes to make sure our codes are comply with PEP style guidance.

10. Try to add the changes again with `git add .` and commit again `git commit -m "chore: demo purpose"`. Then you will see this output
```bash
seed isort known_third_party.............................................Passed
isort (python)...........................................................Passed
black....................................................................Passed
flake8...................................................................Passed
[main b24013e] chore: demo purpose
 5 files changed, 131 insertions(+), 1 deletion(-)
 create mode 100644 .isort.cfg
 create mode 100644 .pre-commit-config.yaml
 rewrite README.md (100%)
 create mode 100644 main.py
 create mode 100644 requirements.txt
```