from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    city: str

person = Person(name="Ariful Islam",age=25,city="Dhaka")

print(person)