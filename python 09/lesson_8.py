# def hello_student(*names):
#     for name in names:
#         print("Привет", name)
        
# def avg(object:list) -> int:
#     "вычисление среднее орифметическое значение из списка и кортежей"
#     print(sum(object) / len(object))
    
# def reverse_word(word:str) -> str:
#     "переварачивает строку"
#     print(word[::-1])
    
# it = "Geeks"

#работа с файлами
# f = open('geeks.txt', 'w')
# f.write("Hello Geeks Backend 09!")
# f.close()

# r = open('geeks.txt', 'r')
# print(r.read())
# r.close()

# py = open('hello.py', 'w')
# py.write("print('Hello World')")
# py.close()

# read_py = open('lesson_2.py', 'r', encoding='utf-8')
# print(read_py.read())
# read_py.close() 

# import os

# folder = r"C:\Users\99677\Desktop\geeks"

# os.rmdir(folder)

# n = 0
# while True:
#     os.mkdir(f"C:\Users\99677\Desktop\hello{n}")
#     if n == 1000:
#         break
    
with open('hello.txt', 'w') as hello:
    hello.write("Hello World")

with open('hello.txt', 'r') as read_file:
    print(read_file.read())

with open('rus.txt', 'w', encoding='utf-8') as rus:
    rus.write("привет мир и гикс!")

with open('students.txt', 'w', encoding='utf-8') as students:
    students.write("Aigerim\n")
    students.write("lol\n")
    
with open('students.txt', 'a', encoding='utf-8') as new_students:
    new_students.write("hahaha\n")


    