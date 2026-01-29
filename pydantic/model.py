from pydantic import BaseModel
from dataclasses import dataclass 

@dataclass
class Person():
    name: str
    age: int
    city: str

person = Person(name="Ariful Islam",age=25,city="Dhaka")

print(person)