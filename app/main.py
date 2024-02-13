from typing import Any


class Car:
    # write your code here
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    # write your code here
    def __init__(self, distance_from_city, clean_power, average_rating, count_of_ratings):
        self.distance_from_city = distance_from_city
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += car.comfort_class * (self.clean_power - car.clean_mark) * (
                            self.average_rating / self.distance_from_city)
                car.clean_mark = self.clean_power

        return round(income, 1)

    def calculate_washing_price(self, car):
        return round(car.comfort_class * (self.clean_power - car.clean_mark) * (self.average_rating / self.distance_from_city), 1)
    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self,rate):
        self.count_of_ratings += 1
        total_ratings_sum = self.average_rating * (self.count_of_ratings - 1) + rate
        self.average_rating = round((total_ratings_sum / self.count_of_ratings),1)




bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')
ford = Car(2, 1, 'Ford')


ws = CarWashStation(6, 8, 3.9, 11)

income = ws.serve_cars([
    bmw,
    audi,
    mercedes
])

# print(ws.calculate_washing_price(ford))
# ws.rate_service(5)
# print(ws.count_of_ratings)
# print(ws.average_rating)
print(income)
# print(ws.calculate_washing_price(bmw))
# print(bmw.clean_mark)
# print(audi.clean_mark)
# print(mercedes.clean_mark)