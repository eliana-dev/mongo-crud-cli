from views import console
from controllers import user_crud
from models.users import find_all_users

if __name__ == "__main__":
    while True:
        console.print_menu()
        option = int(input("Ingrese el numero según la operación que desee realizar: "))
        if option == 1:
            find_all_users()
        elif option == 2:
            user_crud.search_by_username()
        elif option == 3:
            user_crud.insert_user()
        elif option == 4:
            user_crud.update_by_username()
        elif option == 5:
            user_crud.delete_by_username()
        elif option == 6:
            print(" ★ Gracias por usar Mongo Crud Cli")
            break
