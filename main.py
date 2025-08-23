from views import console
from controllers.user_crud import option_manager

if __name__ == "__main__":
    while True:
        console.print_menu()
        if not option_manager() :
         break