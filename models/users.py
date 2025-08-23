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



def find_all_users():
    result = collection.find({}, {"_id": 0})
    for doc in result:
        user = User(**doc)
        print(f"""
          \n------------------------------
          \n USERNAME = {user.username}
          \n NAME = {user.name}
          \n AGE = {user.age}
          \n EMAIL = {user.email}
          \n ----- ADRESS =
            \n\t COUNTRY = {user.adress.country}
            \n\t STATE = {user.adress.state}
            \n\t CITY = {user.adress.city}
            \n\t STREET = {user.adress.street}
            \n\t NUMBER = {user.adress.number}
          """)


def find_username(username):
    result = collection.find_one({"username": username}, {"_id": 0})
    print("""\n====== RESULTADOS de la busqueda =====""")

    user = User(**result)
    print(f"""
          \n------------------------------
          \n USERNAME = {user.username}
          \n NAME = {user.name}
          \n AGE = {user.age}
          \n EMAIL = {user.email}
          \n ----- ADRESS =
            \n\t COUNTRY = {user.adress.country}
            \n\t STATE = {user.adress.state}
            \n\t CITY = {user.adress.city}
            \n\t STREET = {user.adress.street}
            \n\t NUMBER = {user.adress.number}
            \n--------------------------------
          """)
