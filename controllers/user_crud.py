from models.users import User, Adress, find_username, find_all_users
from models.connection import collection
from views import console


def option_manager():
    option = int(input("Ingrese el numero según la operación que desee realizar: "))
    if option == 1:
        find_all_users()
    elif option == 2:
        search_by_username()
    elif option == 3:
        insert_user()
    elif option == 4:
        update_by_username()
    elif option == 5:
        delete_by_username()
    elif option == 6:
        print(" ★ Gracias por usar Mongo Crud Cli")
        return False
    return True

def insert_user():
    # print("------------------------- \n INGRESAR USUARIOS")
    console.print_insert_user()
    username = input("Ingrese el username: ")
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


def search_by_username():
    console.print_find_by_username()
    username = input("Ingrese el username del usuario que desea encontrar: ")
    find_username(username=username)


def update_by_username():
    console.print_update_user()
    username = input("Ingrese el username del usuario que desea actualizar: ")
    filter = {"username": username}
    out_id = {"_id": 0}

    data = collection.find_one(filter, out_id)
    if not data:
        print("Usuario no encontrado.")
        return

    print("Usuario encontrado:", data)

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
        f"Documentos modificados: {res.modified_count}"
    )  # Para mostrar la cantidad de registros que fueron modificados.


def delete_by_username():
    console.print_delete_user()
    username = input("\nIngrese el Username del Usuario que desea eliminar: ")
    filter = {"username": username}
    res = collection.delete_one(filter)
    if res.deleted_count == 0:
        print("Usuario no encontrado.")
        return

    print("Usuario eliminado exitosamente!")
    print(f"Documentos eliminados: {res.deleted_count}")
