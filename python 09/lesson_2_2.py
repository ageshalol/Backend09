#принципы оопю наследственное, полиморфизм, инкапсуляция, и абстракция
# hello = ""
# lst = []
# def hello_world():
#     pass
# hello_world()

# class Hello:
#     pass
# hello = Hello()

# class Person: #родительский класс Person
#     def __init__(self, name, surname, age): #конструктор класса
#         self.name = name #динамический атрибут name
#         self.surname = surname #динамический атрибут surname
#         self.age = age #динамический атрибут age
    
#     def get_info(self): #метод get_info
#         return f"{self.name} {self.surname} {self.age}"
    
# aigerim = Person('Aigerim', 'Sultanova', 15)
# print(aigerim.get_info())

# class Bank(Person): #дочерний класс Bank, которая наследует от класса Person
#     def __init__(self, name, surname, age): #конструктор класса Bank
#         super().__init__(name, surname, age) 
#         self.balance = 0 #новый динамический атрибут balance  с значением 0
        
#     def get_balance(self): #новый метод get_balance 
#             return f"{self.name}, balance {self.balance} KGS"
        
#     def top_up_balance(self, amount):
#         self.balance += amount
#         return f"{self.name}, ваш баланс пополнен на {amount} KGS"
    
#     def withdraw_money(self, amount):
#         if amount == self.balance:
#             self.balance -= amount
#             return f"{self.name}, вы сняли со своего счета {amount} KGS"
#         else:
#              return f"{self.name}, недостачно денег для вывода"
        

# askhat_bank = Bank('lol', 'lolov', 100) #экземпляр класса bank
# print(askhat_bank.get_info()) #вызываем метод get_info
# print(askhat_bank.get_balance()) #вызываем метод get_balance
# print(askhat_bank.top_up_balance(1000))
# print(askhat_bank.get_balance())
# print(askhat_bank.withdraw_money(1000))
# print(askhat_bank.get_balance())

# class Work(Bank):
#     def __init__(self, name, surname, age, work):
#         super().__init__(name, surname, age)
#         self.work = work
        
#     def get_info(self): #переопределение метода get_info
#         return f"Name: {self.name},surname {self.surname}, age {self.age}, balance {self.balance}, work {self.work}" 

# driver_askhat = Work('Askhat', 'lol', 19, 'Driver')
# print(driver_askhat.get_balance())
# print(driver_askhat.top_up_balance(2000))
# print(driver_askhat.get_balance())
# print(driver_askhat.get_info())




#множественное наследование
# class A:
#     def class_a(self):
#         return f"Class A"

# class B:
#     def class_b(self):
#         return f"Class B"
    
# class C(A, B): #множественное наследование
#     pass

# c = C()
# print(c.class_a())
# print(c.class_b())

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0
        self.fuel = 70
        
    def add_distance(self, km):
        self.odometr += km
        
    def subtract_fuel(self, amout):
        self.fuel -= amout
            
    def drive(self, km):
        if (self.fuel * 10) <= km:
            self.add_distance(km)
            self.subtract_fuel(km / 10)         
            return f"Вы проехали {km} km, у вас осталось {self.fuel} литров бензина вы можете проехатьрц            еще {round(self.fuel * 10)} km"
        else:
            return "У вас недостаточно топлива для поездки"
    
camry = Car('toyota', 'camry 55', 2016)
print(camry.drive(350))
print(camry.fuel)