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

classroom = Classroom(
    room_number="A101",
    capacity=30,
    has_projector=True,
    students=["Alice", "Bob", "Charlie"]
)

print(classroom)


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    country: Optional[str] = "USA"

class Customer(BaseModel):
    id: int
    name: str
    email: str
    address: Address

customer = Customer(
    id=1001,
    name="Ariful Islam",
    email="arifcse209@gmail.com",
    address=Address(
        street="123 Main St",
        city="Dhaka",
        state="Dhaka",
        zip_code="1207"
    ))
print(customer)