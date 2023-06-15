#задача 1
# def func():
#     a = input("Ведите фразу: ")
#     isa = a.split()

#     s = ''.join(i[0].upper() for i in isa)
#     print(s)
# func()

# #2
s = {}
def a(b):
    c = b.lower().split(' ')
    for i in c:
        s[i] = c.count(i)
a("Money, money, money, it’s always sunny, in the richmen’s world")
print(s)

#3
def is_isogram(word):
    print(len(word) == len(set(word.lower())))
is_isogram("hello")
is_isogram("world")
is_isogram("Python") 



#4
def hw4(world):
    print(f"<<{world} >> в перевернутом виде <<{world[::-1]}>>")
hw4("nurbolot")

#5
def hw5():
    while True:
        world = input("Введите что то:  ")
        if "?" in world:
            print("конечно!")
        elif "!" in world :
            print("Успокойся!!")
        elif "" or " " in world:
            print("Как классно когда ты молчишь!")
        else:
            print("Ну и что")
