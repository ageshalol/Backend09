#List - списки
#int, bool, str, list, float
# name1 = "Kurmanbek"
# name2 = "Beksultan"
# name3 = "Emir"
# print(name1)
# print(name2)
# print(name3)

names = ["Kurmanbek", "Beksultan", "Emir"]
print(names)

# print(10 + int("20"))

# lst = [10, 1.2, "Hello World", True, False, [1,2,3]] 
# print(lst)

# cars = ["BMW", "TESLA", "HONDA", "FERRARI"]
#           #0      1        2         3
# cars.append("NISSAN")
# print(cars)
# cars.remove("TESLA")
# print(cars)
# print(cars[2])
# cars[0] = "TESLA"
# print(cars)

# it = ["Geeks", "IT Academy", "ProLab", "ONET", "ITC"]
# print(it)
# it.append("IT RUN")
# print(it)
# it.remove("ONET")
# print(it)
# it[4] = "ITC Bootcamp"
# print(it)
# # print(it[::-1])
# # name = "Beksultan"
# print(name[::-1])
# print(it[1:4:2])
# print(it[0:2])

#Tuple - кортеж
# it = ("Geeks", "IT RUN", "ITc", "ITC")
# print(it)
# # tup = (10, 0.1, "Hello", True, (1, 2, 3), [1, 2, 3])
# print(tup)
# print(it.count("Geeks"))
# print(it.index("ITC"))
# # it.append("UDEVS")
# it.remove("Geeks")
# print(it[0])
# print(it[0:2])

# 
# contacts = []
# while True:
#     command = input("1-контакты, 2-добавить, 3-удалить, 4-обновить: ")
#     if command == "1":
#         print(contacts)
#     elif command =="2":
#         add_name = input("Имя: ")
#         contacts.append(add_name)
#         print("Контакт", add_name, "успешно добавлен")
#     elif command == "3":
#         delete_name = input ("имя которую нужно удалить: ")
#         contacts.remove(delete_name)
#         print("контакт", delete_name, "успешно удален")