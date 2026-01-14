'''Задание 1. Инкапсуляция'''
class BankAccount():

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Вносимый баланс д.б. положительным')
        self.__balance += amount

        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(f'Сумма снятия ({amount}) должна быть положительной')
        if amount > self.__balance:
            raise ValueError(f'Недостаточно средств на счете. Доступно: {self.__balance}')
        self.__balance -= amount

        return self.__balance

    def get_balance(self):

        return self.__balance

account = BankAccount()
account.deposit(100)
account.withdraw(-10)
print(account.get_balance())

'''Задание 2. Наследование'''
class Employee(): # Сотрудник

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f'{self.name}, {self.position}, {self.salary}'

class Developer(Employee): # Разработчик

    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        return f'{super().get_info()}, {self.programming_language}'

class Manager(Employee): # Менеджер

    def __init__(self, name, position, salary, list_of_employees: list):
        super().__init__(name, position, salary)
        self.list_of_employees = list_of_employees

    def get_info(self):
        team = []
        for employee in self.list_of_employees:
            team.append(employee.get_info())

        return (f'Manager:\n'
                f'{super().get_info()}\n'
                f'Team:\n'
                f'{"\n".join(team)}')

print(Developer('Alex', 'Middle', '300 000', 'Python').get_info())

Employee_1 = Employee('Bob', 'Инженер', '120 000')
Employee_2 = Employee('Tom', 'Механик', '150 000')
Employee_3 = Employee('John', 'Садовник', '180 000')
print(Manager('Sergey', 'Manager', '500 000', [Employee_1, Employee_2, Employee_3]).get_info())

'''Задание 3. Полиморфизм'''
class Shape():
    def area(self):
        return 0

    def perimeter(self):
        return 0

class Rectangle(Shape): # Прямоугольник
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

class Circle(Shape): # Круг
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2) # Площадь круга Pi*r**2

    def perimeter(self):
        return 2 * 3.14 * self.radius # Длина окружности 2*Pi*r

def fun1(rect, circ):
    list_of_shapes = []
    list_of_shapes.extend([rect, circ])

    for shape in list_of_shapes:
        print(shape.area(), shape.perimeter())

fun1(Rectangle(5, 6), Circle(4))

'''Задание 4. Абстракция и интерфейс'''
from abc import ABC, abstractmethod

class Transport(ABC):

    @abstractmethod
    def start_engine(self) :
        pass

    @abstractmethod
    def stop_engine(self) :
        pass

    @abstractmethod
    def move(self):
        pass

class Car(Transport):

    def start_engine(self) :
        return f'Тачка завелась'

    def stop_engine(self) :
        return f'Тачка выключила двигатель'

    def move(self):
        return f'Тачка поехала'

class Boat(Transport):

    def start_engine(self):
        return f'Лодка завелась'

    def stop_engine(self):
        return f'Лодка выключила двигатель'

    def move(self):
        return f'Лодка поехала'

'''Задание 5. Множественное наследование'''
class Flyable():

    def fly(self):
        return f'Im flying!'

class Swimmable():

    def swim(self):
        return f'Im swimming!'

class Duck(Flyable, Swimmable):

    def make_sound(self):
        return f'Quack!'

duck = Duck()
print(duck.fly(), duck.swim(), duck.make_sound())

'''(Дополнительно) Задание 6. Комбинированное: Зоопарк'''
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):

    def speak(self):
        return f'Woof!'

    def move(self):
        return f'Собака бегает'

class Bird(Animal, Flyable):

    def speak(self):
        return f'Tweet!'

    def move(self):
        return self.fly()

class Fish (Animal, Swimmable):

    def speak(self):
        return f'Рыба молчит'

    def move(self):
        return self.swim()

def fun2():
    list_of_animals = [Dog(), Bird(), Fish()]

    for animal in list_of_animals:
        print(f'{animal.speak()}. {animal.move()}')

fun2()

'''1. Singleton'''
class Logger():
    _instance = None # Экземпляр еще не создан, если True - то создан
    logs = []

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance

    def log(self, message: str):
        self.logs.append(message)

    def get_logs(self):
        return self.logs

logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

assert logger1 is logger2, "Logger is not a singleton!"
assert logger1.get_logs() == ["First message", "Second message"]

'''2. SOLID'''
class Report():

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_pdf(self):
        print("PDF generated")

    def save_to_file(self, filename):
        print(f"Saved {filename}")

class FIleStorage():

    def __init__(self, title, content):
        self.data_base = []
        self.title = title
        self.content = content

    def save_to_data_base(self, title, content):
        data_base.append([title, content])

        return f'Saving {title}, {content}'

class PdfGenerator():

    def generate_pdf(self):
        return f'PDF generated'

class FileSaver():

    def save_to_file(self, filename):
        return f'Saved {filename}'

'''3. SOLID (O)'''
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class PaymentService():

    def __init__(self, gateway: PaymentProcessor):
        self.gateway = gateway

    def process_payment(self, amount):
        success = self.gateway.pay(amount)
        if success:
            return f'Оплата прошла успешно'

        return f'Ошибка при оплате'

class PayPal(PaymentProcessor):

    def pay(self, amount):
        return f'Оплата {amount} по PayPal'

class CreditCard(PaymentProcessor):

    def pay(self, amount):
        return f'Оплата {amount} по кредитке'

class Crypto(PaymentProcessor):

    def pay(self, amount):
        return f'Оплата {amount} по Crypto'

paypal_gateway = PayPal()
payment_service_paypal = PaymentService(paypal_gateway)
payment_service_paypal.process_payment(20)


credit_card_gateway = CreditCard()
payment_service_credit_card = PaymentService(credit_card_gateway)
payment_service_credit_card.process_payment(40)


crypto_gateway = Crypto()
payment_service_crypto = PaymentService(crypto_gateway)
payment_service_crypto.process_payment(60)

'''5. SOLID (I)'''
from abc import ABC, abstractmethod

class Animal():

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def swim(self):
        pass

class Lion(Animal):

    def fly(self):
        pass

    def run(self):
        return f'Лев бежит'

    def swim(self):
        pass

'''4. SOLID (L)'''
from abc import ABC, abstractmethod

class Bird(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        pass

    def eat(self):
        return f'{self.name} ест'

class Sparrow(Bird):

    def move(self):
        return f'{self.name} летит'

    def fly(self):
        return f'{self.name} летает высоко'

class Penguin(Bird):

    def move(self):
        return f'{self.name} плавает'

    def swim(self):
        return f'{self.name} плавает быстро'

def bird_activity(bird: Bird):
    return f'{bird.move()}. {bird.eat()}.'

sparrow = Sparrow('Воробей')
penguin = Penguin('Пингвин')

print(bird_activity(sparrow))
print(bird_activity(penguin))

'''6. staticmethod, classmethod, property'''
class Temperature:

    def __init__(self, celsius):
        self._celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        return cls((fahrenheit - 32) * 5 / 9) # Фаренгейты в Цельсии

    @property
    def kelvin(self):
        return self._celsius + 273.15 # Т-ра в Кельвинах

    @staticmethod
    def is_freezing(celsius):
        return celsius <= 1

    def __str__(self):
        return f'{self._celsius}°C'