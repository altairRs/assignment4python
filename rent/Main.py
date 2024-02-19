from user_service import UserService
from car import Car
from rental_service import RentalService
from csv_manager import CSVManager

def main():
    user_service = UserService()
    service = RentalService()
    cars_data = CSVManager.load_data_from_csv('cars.csv')

    for car_data in cars_data:
        service.add_item(car_data)

    while True:
        print("\n1. Login")
        print("2. Register")
        print("3. Admin Login")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, username = user_service.login(username, password)
            if success:
                if username != 'admin':
                    user_menu(service, username)
                else:
                    admin_menu(user_service, service)

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_service.register(username, password)

        elif choice == '3':
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            success, username = user_service.login(username, password)
            if success and username == 'admin':
                admin_menu(user_service, service)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

def user_menu(service, username):
    pass

def admin_menu(user_service, service):
    while True:
        print("\nAdmin Menu:")
        print("1. View User Information")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_service.view_user_info()

        elif choice == '2':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
