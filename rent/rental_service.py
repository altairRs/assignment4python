class RentalService:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def find_item(self, keyword):
        found_items = []
        for item in self.items:
            if keyword.lower() in item['name'].lower():
                found_items.append(item)
        return found_items

    def show_all_cars(self):
        if self.items:
            print("Existing Cars:")
            for idx, item in enumerate(self.items, start=1):
                print(f"{idx}. Name: {item['name']}, Model: {item['model']}, Year: {item['year']}, Price per Day: {item['price_per_day']}")
        else:
            print("No cars in the rental service.")

    def rent_car(self, car_id):
        if 0 < car_id <= len(self.items):
            car = self.items[car_id - 1]
            if not car.get('is_rented'):
                car['is_rented'] = True
                return True, None
            else:
                return False, "Car is already rented"
        else:
            return False, "Invalid car ID"

    def calculate_payment(self, car_id, days):
        if 0 < car_id <= len(self.items):
            car = self.items[car_id - 1]
            if car.get('is_rented'):
                return car['price_per_day'] * days
            else:
                return 0
        else:
            return 0


