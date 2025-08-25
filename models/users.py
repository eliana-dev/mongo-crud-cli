from pydantic import BaseModel
from models.connection import collection

class Adress(BaseModel):
    country: str
    state: str
    city: str
    street: str
    number: int


class User(BaseModel):
    username: str
    name: str
    age: int
    email: str
    adress: Adress

    def save(self):
      
        collection.insert_one(self.model_dump())
