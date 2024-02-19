import csv

class CSVManager:
    @staticmethod
    def load_data_from_csv(filename):
        try:
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                return [{k: float(v) if k == 'price_per_day' else v for k, v in row.items()} for row in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_data_to_csv(data, filename):
        fieldnames = ['name', 'model', 'year', 'price_per_day', 'is_rented']
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        except Exception as e:
            print("Error occurred while saving data to CSV:", e)

