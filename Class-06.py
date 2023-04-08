#1
class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b


calc = Calculator(12, 24)
s = calc.add()
m = calc.sub()
print(s, m)

#2
class Calculator:
    def add(self, a, b):
        return a+b

    def sub(slef, a, b):
        return a-b


class Square(Calculator):
    def sqr(self, a):
        return a*a


my_calc = Square()
s = my_calc.add(12, 24)
print(s)

#3
class Calculator:
    def add(self, a, b):
        return a+b

    def sub(slef, a, b):
        return a-b


class Sum(Calculator):
    def add(self, a, b, c):
        return a+b+c


my_calc = Sum()
s = my_calc.add(12, 24, 5)
print(s)

#4
class Employee:
    def __init__(self, name):
        self.name = name

    def income(self, money=None):
        self.money = money
        if money == None:
            print(f"{self.name} is poor enough")
        elif money > 50:
            print(f"{self.name} is not poor")
        else:
            print(f"{self.name} is rich")


me = Employee("Plabon")
me.income(94)

#5
from abc import ABC, abstractmethod


class Month(ABC):
    @abstractmethod
    def weeks(self):
        pass

    @abstractmethod
    def days(self):
        pass


class January(Month):
    def weeks(self):
        print("4")

    def days(self):
        print("31")


m = January()
m.days()
m.weeks()

#6
class Student:
    def __init__(self):
        self.name = "Emon"
        self._age = 20
        self.__session = 2018

    def get_session(self):
        print(self.__session)

    def set_session(self, session):
        self.__session = session


s = Student()
print(s.get_session())

s.set_session(2020)
print(s.get_session())
# print(s._age)
# print(s.__session)

#7
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width*self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())

#8
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True


ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)


