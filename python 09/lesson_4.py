#циклы for и while
# print("Hello world 1")
# print("Hello world 2")
# print("Hello world 3")
# print("Hello world 4")
# print("Hello world 5")
# print("Hello world 6")
# print("Hello world 7")

# for i in range(100):
#     print("Hello World", i)
    
# for n in range(1001):
#     print(n)
#     print("Geeks")
    
# for day in range(1, 32):
#     print("Утро")
#     print("День", day)
#     print("Ночь")
#     print("==============")
    
# number = int(input("Number: "))
# if number % 2 == 0:
#     print(number, "четный")
# else:
#     print(number, "нечетный") 

# chet_numbers = []
# for numbers in range(2, 101, 2):
#     chet_numbers.append(numbers)
# print(chet_numbers)

# numbers = [10, 11, 13, 1001, 1002, 1010, 3, 4, 66, 88, 90, 103, 507, 809, 104,]
# chet = []
# for num in numbers: #итерация списка  numbers
#     if num % 2 == 0:
#         chet.append(num)
# print(chet)

# names = ["Kurmanbek", "Nurbolot", "Janysh", "asylbek", "Askhat"]
# print(names)
# for name in names:
#     print(name)
    
# num1 = 10
# num2 = 20
# while num1 < num2:
#     num1 += 1
#     print(num1)

# shet = 0
# while True:
#     shet += 1
#     print(shet)
#     #ctrl + c
    
# n = 0
# while True:
#     n += 10
#     print(n)
#     if n == 1004:
#         print("HACKED!!!")
#         break 
    
# import time 

# k = 0
# while True:
#     k += 10
#     print("HACK", k, "%")
#     if k == 100:
#         print("HACK SYSTEM")
#         break
#         time.sleep(5)
        
import random

print(random.randint(1, 10))

random_number = random.randint(1, 10)
attempts = 5
while True:
    user_number = int(input("Ведите число с 1 до 10: "))
    attempts -= 1
    if user_number == random_number:
        print("WIN!!!")
        break
    elif attempts == 0:
        print("LOSE!!!")
        break
    elif user_number >10:
        print("Число больше 10")
    else:
        print("WRONG ANSWER", attempts, "attempts")
    
