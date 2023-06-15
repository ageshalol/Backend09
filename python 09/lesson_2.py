# print("Hello Geeks and python")

# str_example_1 = 'Hello I\'m backend developer'
# print(str_example_1)

# str_example_2 = "Hello, Im backend developer"
# print(str_example_2)

# str_example_3 = """Hello, Im backend developer
# Language Python"""
# print(str_example_3)

# str_example_4 = '''Hello I'm backend developer
# Language Python'''
# print(str_example_4)

#конкатентенция - это склеивания строк через оператор + 
print("Nurbolot" + " " + 'Erkinbaev')
print("Nurbolot " + "Erkinbaev")
print("Nurbolot", 'Erkinbaev')

# name = input("Имя:")
# print("Привет", name)

# it = "Geeks " #индексы строк
#       #01234
# print(it[3])
# print(it[0])
# print(it[5])

# print(it[0:4])

# Language = "Python"
#            #012345
# print(Language[0:2])
# print(Language[::2])

#условие if, elif, else
# num1 = 100
# num2 = 1002
# if num1 > num2:
#     print("переменная num1 больше")
# elif num1 == num2:
#     print("Равны")
# else:
#     print("переменная num2 больше")
    
#операторы сравнения (6)
# print(30 == 30)
# print(40 == 10)

# print(20 != 5)
# print(10 != 10)

# print(30 > 3)
# print(30 > 100)

# print(40 < 4)
# print(40 < 40)

# print(40 <= 40)
# print(40 <= 100)

# print(50 >=100)
# print(60 >=60)

# age =int(input("ваш возраст: "))
# if age < 14: 
#     print("извинитеб ваш возраст не подхходит")
# else:
#     print("добро пожаловать на курсы geeks")
    
# Login = input("Login: ")
# password == input("password: ")
# if Login =="geeks" or password == "geeksstudents":
#     print("welcome")
# else:
#     print("Error")

num1 = 1001
num2 = 1002
num3 = 1003 
if num1 > num2 and num1 > num3:
    print('num1 больше')
elif num2 > num1 and num2 > num3:
    print('num2 больше')
elif num3 > num1 and num3 > num2:
    print('num3 больше')
else:
    print("Они все равны")