from typing import Optional, List

from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int
    city: str

person = Person(name="Ariful Islam",age=25,city="Dhaka")

print(person)


class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: Optional[float] = None
    is_active: Optional[bool] = True

employee = Employee(id=1, name="Ariful Islam", department="Engineering", salary=75000.0)
print(employee)

class Classroom(BaseModel):
    room_number: str
    capacity: int
    has_projector: Optional[bool] = False
    students: List[str]