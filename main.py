from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


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
