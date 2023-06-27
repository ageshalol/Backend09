#ооп - обьект-орионтированное програмиророванние
# class Car():
#     brand = "Toyota" #атрибут toyota с значением Toyota
#     model = "Prius" #атрибут model c значением Prius  
    
#     def drive(self): #метод drive внутри класса Car
#         #self -  это стандартное имя первого аргумента для создания методов
#         print("Drive Car") #выводим значение Drive Car
        
#     def stop_car(self): #метод stop_car
#         print("Stop Car") #выводим значение stop car
            
# car = Car()  #объект или кземпляр класса Car
# print(car)
# print(car.brand) #вызываем атрибут brand c классом Car
# print(car.model) #вызываем атрибут model c классом Car
# car.drive() #вызываем метод drive через объект класса car (10 line)
# car.stop_car() #вызываем метод stop_car через объект класса car (10 line)

# def welcome(name:str) -> str:
#     return f"Welcome {name}"
# print(welcome("Aigerim"))

class Airplane: #динамические класс Airplane
    def __init__(self, name, passengers_seats, weigth): #конструктор
        self.name = name
        self.passengers_seats = passengers_seats
        self.weigth = weigth
        self.odometr = 0
        self.is_flying = False
    
    def info(self):
        return f"{self.name}, {self.passengers_seats}, {self.weigth} {self.odometr} {self.odometr} {self.is_flying}"
    
    def fly(self):
        if self.is_fluing == False:
            self.is_flying = True
            return f"НАчинаем взлет самолета {self.name}"
        else:
            return f"у вас уже заведен двигатель"
    
    def flying(self, km):
        if self.if_flying == True:
            self.odometr += km
            return f"вы прилетели на самолете {self.name}, {km} km"
        else:
            return "у вас отключены двигатели"
    
    def landing(self):
        if self.if_flying == True:
            self.is_flying = False
            return f"вы сделали посадку самолета, двигатели отлючены"
        else:
            return "вы не сможете сделать посадку"
    
     
boeing_747 = Airplane("Boeing 747", 660, 183500)
print(boeing_747.info())
print(boeing_747.fly())
print(boeing_747.flying(300))
print(boeing_747.info())
print(boeing_747.flying(300))
print(boeing_747.info())
print(boeing_747.landing())
print(boeing_747.info())
print(boeing_747.flying(300))

        
