import pickle
from datetime import datetime

class Car:
    def __init__(self, name: str, release_date: str, sell_date: str):
        self.name = name
        self.release_date = release_date
        self.sell_date = sell_date

    def __str__(self):
        return "Name: {}, release date: {}, sell date: {}".format(self.name, self.release_date, self.sell_date)


def enter_mode():
    file_mode = input("Enter 'w' to overwrite file or 'a' to append information to file: ")
    while file_mode != 'w' and file_mode != 'a':
        file_mode = input("Incorrect input. Enter 'w' to overwrite file or 'a' to append information to file: ")
    return file_mode + "b"


def creating_first_file(path : str, mode: str):
    line = input("Enter cars in format: name DD.MM.YYYY(release date) DD.MM.YYYY(sell date).\n"
                 "To finish entering go to a new line and press <Ctrl + S>:\n")
    with open(path, mode) as file:
        while line != "aaa":
            if line:
                splitted = line.split()
                name = str()
                for info in splitted[:len(splitted)-2]:
                    name += info + " "
                name = name.rstrip(name[-1])
                release_date = splitted[len(splitted)-2]
                sell_date = splitted[-1]
                car = Car(name, release_date, sell_date)
                pickle.dump(car, file)
            line = input()


def creating_second_file(first_path: str, second_path: str):
    with open(first_path, 'rb') as first_file:
        with open(second_path, "wb") as second_file:
            while True:
                try:
                    car = pickle.load(first_file)
                    if datetime.now().month == int(car.sell_date.split('.')[1]) and datetime.now().year == int(car.sell_date.split('.')[2]):
                        pickle.dump(car, second_file)
                except EOFError:
                    break


def read_cars(path: str):
    with open(path, 'rb') as file:
        while True:
            try:
                print(pickle.load(file))
            except EOFError:
                break


def output_used_cars(file_path: str):
    car_list = list()
    with open(file_path, "rb") as file:
        while True:
            try:
                car_list.append(pickle.load(file))
            except EOFError:
                break
    print("\nUsed cars:")
    for car in car_list:
        splitted_sell = car.sell_date.split(".")
        s_day = int(splitted_sell[0])
        s_month = int(splitted_sell[1])
        s_years = int(splitted_sell[2])
        splitted_release = car.release_date.split(".")
        r_day = int(splitted_release[0])
        r_month = int(splitted_release[1])
        r_years = int(splitted_release[2])
        delta_year = s_years - r_years
        delta_month = s_month - r_month
        delta_day = s_day - r_day
        if delta_year > 1 or (delta_year == 1 and delta_month > 0) or (delta_year == 1 and delta_month == 0 and delta_day > 0):
            print(car)