from user_service import UserService
from car import Car
from rental_service import RentalService
from csv_manager import CSVManager
from initial_car_loader import InitialCarLoader

def main():
    user_service = UserService()
    service = RentalService()

    initial_cars = InitialCarLoader.load_initial_cars()
    for car_data in initial_cars:
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
    while True:
        print("\nUser Menu:")
        print("1. Rent a Car")
        print("2. View Rented Cars")
        print("3. Sort Cars by price")
        print("4. Sort Cars by year")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            service.show_all_cars()
            car_id = int(input("Enter the ID of the car you want to rent: "))
            days = int(input("Enter the number of days for rent: "))
            card_number = input("Enter your card number: ")
            expiry_date = input("Enter expiry date (MM/YY): ")
            cvv = input("Enter CVV: ")
            success, total_payment = service.rent_car(car_id, username, days, card_number, expiry_date, cvv)
            if success:
                print(f"Total payment: {total_payment}")
                print("Please enter your payment information:")
                print("Thank you for your payment!")
            else:
                print(total_payment)

        elif choice == '2':
            rented_cars = service.get_user_rented_cars(username)
            if rented_cars:
                print("Your rented cars:")
                for idx, car_info in enumerate(rented_cars, start=1):
                    print(f"{idx}. Name: {car_info['car']['name']}, Model: {car_info['car']['model']}, "
                          f"Year: {car_info['car']['year']}, Price per Day: {car_info['car']['price_per_day']}, "
                          f"Payment Info: {car_info['payment_info']}")
            else:
                print("You haven't rented any cars yet.")

        elif choice == '3':
            sorted_cars = service.sort_cars_by_price()
            print("Cars sorted by price:")
            for idx, car in enumerate(sorted_cars, start=1):
                print(f"{idx}. Name: {car['name']}, Model: {car['model']}, Year: {car['year']}, "
                      f"Price per Day: {car['price_per_day']}")

        elif choice == '4':
            sorted_cars = service.sort_cars_by_year()
            for idx, car in enumerate(sorted_cars, start=1):
                print(f"{idx}. Name: {car['name']}, Model: {car['model']}, Year: {car['year']}, "
                      f"Price per Day: {car['price_per_day']}")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")


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
