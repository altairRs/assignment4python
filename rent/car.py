class Car:
    def __init__(self, name, model, year, price_per_day):
        self.name = name
        self.model = model
        self.year = year
        self.price_per_day = price_per_day

    def to_dict(self):
        return {
            'name': self.name,
            'model': self.model,
            'year': self.year,
            'price_per_day': self.price_per_day
        }
