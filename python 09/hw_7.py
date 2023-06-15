# hw 1
# def hello(x):
#   print(x * x - 10)
# hello = lambda x: x * x - 10
# print(hello(5))

# #hw 2
# name = ["Kuma", "Nurtilek", "Zina", "Edzen", "Kuma", "Aitenur", "Zina"]
# name = list(filter(lambda x: name.count(x) == 1, name))
# print(name)
         
#hw 3
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda nums: nums % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# hw 4
# names = ["azat", "zina", "kuma", "anna", "sas"]
# palindromes = list(filter(lambda x: x == x[::-1], names))
# print(palindromes)

# hw 5 
# time1 = input("Введите первую отметку времени в формате чч:мм:сс: ")
# time2 = input("Введите вторую отметку времени в формате чч:мм:сс: ")

# h1, m1, s1 = map(int, time1.split(":"))
# h2, m2, s2 = map(int, time2.split(":"))

# total_seconds1 = h1 * 3600 + m1 * 60 + s1
# total_seconds2 = h2 * 3600 + m2 * 60 + s2

# difference = total_seconds2 - total_seconds1

# print(f"Разница между отметками времени составляет {difference} секунд")
