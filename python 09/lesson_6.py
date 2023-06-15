#Functions - функции
# print()
# len()
# input()
# #это встроенные функции


# print("Hello Geeks")
# def hello(): #пользовательское функция hello. Создается с помощью оператора def
#     print("Hello World")
#     print("Geeks")
# # hello()

# def welcome():
#     name = input("Name: ")
#     print(f"Welcome {name}!")
# welcome()

# def calculator():
#     num1 = int(input("Number1: "))
#     operator = input("+, -, *, /: ")
#     num2 = int(input("Number2: "))
#     if operator == "+":
#         print(f"Result {num1 + num2}")    
#     elif operator == "-":
#         print(f"Result {num1 - num2}")
#     elif operator == "*":
#         print(f"Result {num1 * num2}")
#     elif operator == "/":
#         print(f"Resul {num1 / num2}")
#     else:
#         print("Error operator")
# calculator()

# def add(num1, num2): #num1, num2 являются параметрами функции add
#     print(num1 + num2)
# add(10, 20)
# add("10", "20") #значение 10 и 20 явяляются аргументами

# def mult(num1:int, num2:int):
#     print(num1 * num2)
# mult(10, 20)
# mult("Geeks", 3)
 
# def sub(num1:int, num2:int) -> int:
#     print(num1 - num2)
# sub(20, 10)

# def div(num1:int=1, num2:int=2) -> float:
#     "данная функция принимает два числа и делит их" 
#     print(num1 / num2)
# div()
# div(20)

# import random

# def generator_passworld(len_passworld:int=8) -> str:
#     letters = "qwertyuiopasdfghjklzxcvbnm1234567890@!#$%^Y&*()_"
#     result = ""
#     for n in range(len_passworld):
#        random_letter = random.choice(letters)
#        result += random_letter
#     print(result)
# generator_passworld(20)
# generator_passworld(4)
# generator_passworld(15)

#исключения try, except
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("на ноль делить нельзя!")
    
# try:
#    print("10" + 10)
# except ZeroDivisionError:
#     print("ошибка типов данных")
    
# def calculator(num1:int=1, operator:str="+", num2:int=1):
#     try:
#         num1 = int(input("Number1: "))
#         operator = input("+, -, *, /: ")
#         num2 = int(input("Number2: "))
#         if operator == "+":
#             print(f"Result {num1 + num2}")    
#         elif operator == "-":
#             print(f"Result {num1 - num2}")
#         elif operator == "*":
#             print(f"Result {num1 * num2}")
#         elif operator == "/":
#             try:
#                 print(f"Resul {num1 / num2}")
#             except ZeroDivisionError:
#                 print("На ноль делить нельзя!")
#         else:
#             print("Error operator")
#     except TypeError:
#         print("Ошибка")
# calculator(20, "+", 20)
# calculator(10, "/", 0)

# raise ValueError("Hello world")

