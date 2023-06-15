#1 импортировать сам модуль
import lesson_8

lesson_8.avg([1, 2, 3, 4, 5])
lesson_8.reverse_word("Geeks")
lesson_8.hello_student("Aigerim", "Gesha", "lol")

#2. импортировать отдельные определения из модуля
# from lesson_8 import avg, reverse_word

# avg((10, 20, 30, 40, 50))
# avg((2, 2, 2, 3, 3, 3, 4, 5))
# reverse_word("Aigerim")

#3. импортировать все содержимое модуля сразу
# from lesson_8 import *

# avg((2, 2, 2, 3, 3))
# reverse_word("Aigerim")
# hello_student("llooll", "haha")
# avg((10, 20 , 30, 40, 50))
# print(it)
