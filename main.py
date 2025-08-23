from views import console
from controllers import user_crud
if __name__ == "__main__":
    while True:
        console.print_menu()
        user_crud.options_manager()