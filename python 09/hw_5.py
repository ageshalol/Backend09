  #задача 1
# if __name__ == '__main__':
#     dictionary_1 = {'a': 300, 'b': 400} 
#     dictionary_2 = {'c': 500, 'd': 600}
#     dictionary_1.update(dictionary_2)
#     print(dictionary_1)
    
#задача 2
# numbers = {'num_1' : 1, 'num_2' : 2, 'num_3' : 3, 'num_100' : 100}
# result=1
# for key in numbers:
#     result=result * numbers[key]
# print(result)

#задача 3
# student = {'name' : 'Askhat', 'age' : 17}
# student['age'] *= 2
# print(student)

#задача 4
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# student['age'] = 16
# print(student)

#задача 5
# student = {'name' : 'Askhat', 'age' : 17}
# student.pop('age')
# print(student)

#задача 6
# student = {'name' : 'Askhat'}
# student['address'] = 'Западный Анар'
# print(student)

#задача 7
# password = input()
# password2 = input()
# while len(password) < 8:
#     print("Короткий пароль!")
#     password = input()
#     password2 = input()
# while "123" in password:
#     print("Простой пароль!")
#     password = input()
#     password2 = input()
# while password2 != password:
#     print("Различаются.")
#     password = input()
#     password2 = input()
# else:
#     print("OK, Пароль создан!")