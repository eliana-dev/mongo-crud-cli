from models.users import User, Adress
from models.connection import collection
from views import console
from colorama import Fore, Style


def option_manager():
    while True:
        option = input("Ingrese el numero según la operación que desee realizar: ")
        if option.isdigit() and 1 <= int(option) <= 6:
            option = int(option)
            break
        else:
            print(Fore.RED + "Ingrese un numero de la lista de opciones")
    if option == 1:
        find_all_users()
    elif option == 2:
        find_by_username()
    elif option == 3:
        if confirm_operation():
            print(Fore.LIGHTGREEN_EX + "Operacion confirmada!")
            insert_user()
        else:
            print(Fore.LIGHTRED_EX + "Operación cancelada")
    elif option == 4:
        if confirm_operation():
            print(Fore.LIGHTGREEN_EX + "Operacion confirmada!")
            update_by_username()
        else:
            print(Fore.LIGHTRED_EX + "Operación cancelada")
    elif option == 5:
        if confirm_operation():
            print(Fore.LIGHTGREEN_EX + "Operacion confirmada!")
            delete_by_username()
        else:
            print(Fore.LIGHTRED_EX + "Operación cancelada")
    elif option == 6:
        print(" ★ Gracias por usar Mongo Crud Cli")
        return False
    return True


def confirm_operation():
    while True:
        confirm = input(Style.DIM + "Desea confirmar la operación? [y/n]: ").lower()
        if confirm == "y":
            return True
        elif confirm == "n":
            return False
        else:
            print("Solo puede ingresar 'y' o 'n'.")


def insert_user():
    console.print_insert_user()
    username = input("Ingrese el Nombre de usuario: ")
    name = input("Ingrese el Nombre: ")
    age = int(input("Ingrese la Edad: "))
    email = input("Ingrese el Email: ")
    country = input("Ingrese el Pais: ")
    state = input("Ingrese el Estado : ")
    city = input("Ingrese la Ciudad: ")
    street = input("Ingrese la Calle: ")
    number = int(input("Ingrese el Numero de calle: "))

    adress = Adress(
        country=country, state=state, city=city, street=street, number=number
    )
    user = User(
        username=username,
        name=name,
        age=age,
        email=email,
        adress=adress,
    )
    user.save()


def find_by_username():
    console.print_find_by_username()
    username = input("Ingrese el nombre de usuario que desea buscar: ")
    data = collection.find_one({"username": username}, {"_id": 0})
    if not data:
        print(Fore.RED + "Usuario no encontrado.")
        return

    print(Fore.LIGHTBLUE_EX + """\n====== RESULTADOS de la busqueda =====""")

    user = User(**data)
    print(Fore.LIGHTGREEN_EX + "\n------------------------------")
    print(f"""
          \n USERNAME = {user.username}
          \n NAME = {user.name}
          \n AGE = {user.age}
          \n EMAIL = {user.email}
          \n ----- ADRESS =
            \n\t COUNTRY = {user.adress.country}
            \n\t STATE = {user.adress.state}
            \n\t CITY = {user.adress.city}
            \n\t STREET = {user.adress.street}
            \n\t NUMBER = {user.adress.number}""")
    print(Fore.LIGHTGREEN_EX + "\n------------------------------")
    

def find_all_users():
    console.print_find_all()
    result = collection.find({}, {"_id": 0})
    for doc in result:
        user = User(**doc)
        print(Fore.LIGHTGREEN_EX + "\n------------------------------")
        print(f"""
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


def update_by_username():
    console.print_update_user()
    username = input("Ingrese el nombre de usuario para actualizar los datos: ")
    filter = {"username": username}
    out_id = {"_id": 0}

    data = collection.find_one(filter, out_id)
    if not data:
        print(Fore.RED + "Usuario no encontrado.")
        return

    print(Fore.LIGHTBLUE_EX + "Usuario encontrado:\n", data)

    print(
        "------------------------- \n INGRESAR NUEVOS DATOS (deje vacío para no cambiar)"
    )
    # short circuit evaluation con or
    # pide el valor por input si el valor es "" lo toma como false y toma como valor por defecto lo que esta despues de or
    # c = a or b -----> si a = false entonces c = b pero si a = true entonces c = a
    username = input(f"Username [{data['username']}]: ") or data["username"]
    name = input(f"Nombre [{data['name']}]: ") or data["name"]
    age = input(f"Edad [{data['age']}]: ") or data["age"]
    email = input(f"Email [{data['email']}]: ") or data["email"]
    country = (
        input(f"País [{data['adress']['country']}]: ") or data["adress"]["country"]
    )
    state = input(f"Estado [{data['adress']['state']}]: ") or data["adress"]["state"]
    city = input(f"Ciudad [{data['adress']['city']}]: ") or data["adress"]["city"]
    street = input(f"Calle [{data['adress']['street']}]: ") or data["adress"]["street"]
    number = input(f"Número [{data['adress']['number']}]: ") or data["adress"]["number"]

    update = {
        "$set": {
            "username": username,
            "name": name,
            "age": int(age),
            "email": email,
            "adress": {
                "country": country,
                "state": state,
                "city": city,
                "street": street,
                "number": int(number),
            },
        }
    }

    res = collection.update_one(filter, update)
    print(
        Fore.LIGHTYELLOW_EX + f"Documentos modificados: {res.modified_count}"
    )  # Para mostrar la cantidad de registros que fueron modificados.


def delete_by_username():
    console.print_delete_user()
    username = input("\nIngrese el nombre de usuario para eliminar los datos: ")
    filter = {"username": username}
    out_id = {"_id": 0}
    data = collection.find_one(filter, out_id)
    if not data:
        print(Fore.RED + "Usuario no encontrado.")
        return
    print(
        Fore.LIGHTBLUE_EX + "Usuario encontrado:\n", data
    )  # asi vemos que usuario estamos por eliminar
    res = collection.delete_one(filter)
    if res.deleted_count == 0:
        print(Fore.RED + "Usuario no encontrado.")
        return

    print("Usuario eliminado exitosamente!")
    print(Fore.LIGHTYELLOW_EX + f"Documentos eliminados: {res.deleted_count}")
