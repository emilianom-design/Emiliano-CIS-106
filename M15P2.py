class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return 0.90 * self.sticker_price

class Sportcar(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = "N"
        self.sport_engine = "N"
        self.sport_interior = "N"

    def set_sport_wheels(self, option):
        self.sport_wheels = option.upper()

    def set_sport_engine(self, option):
        self.sport_engine = option.upper()

    def set_sport_interior(self, option):
        self.sport_interior = option.upper()

    def updated_price(self):
        price = self.discount_price()
        if self.sport_wheels == "Y":
            price += 1000.00
        if self.sport_engine == "Y":
            price += 3000.00
        if self.sport_interior == "Y":
            price += 2000.00
        return price

car1 = Car('Toyota', 'Camry', 30000.00)
car2 = Car('Honda', 'Civic', 25000.00)

sport1 = Sportcar('Ford', 'Mustang', 40000.00)
sport1.set_sport_wheels('Y')
sport1.set_sport_engine('N')
sport1.set_sport_interior('Y')

sport2 = Sportcar('Chevy', 'Corvette', 60000.00)
sport2.set_sport_wheels('Y')
sport2.set_sport_engine('Y')
sport2.set_sport_interior('Y')

print(car1.make, car1.model, car1.discount_price())
print(car2.make, car2.model, car2.discount_price())

print(sport1.make, sport1.model, sport1.updated_price())
print(sport2.make, sport2.model, sport2.updated_price())
