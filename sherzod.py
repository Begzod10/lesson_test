# Data types
# string = ""
# integer  = sonlar
# list = []
# object, dictionary = {}
# float = 12.5
# boolean = True, False

# name = "SherzodKuzko"
# name = int(input('Enter name '))
# print(type(name))
# if name == "Sherzod":
#     print("tog'ri")
# elif name == "SherzodKuzko":
#     print("ha u kuzko")
# else:
#     print("notog'ri")
# buyruqlar = ["yugur", "yugur"]
# index = buyruqlar.count("yugur")
# print(index)
# if
# if
# if
#       0123456
# name = "Sherzod tente"
# print(name.upper()) hamma harfini kotta qberadi
# print(name.lower()) hamma harfini kichkina qberadi
# print(name.capitalize()) birinchi harfini kotta qberadi
# print(len(name)) textni harflarini sanab beradi
# print(name.find("z")) harfni indexsini topib beradi
# new_name = name.replace("tente", "aqlli") 2 ta so'zni almashtirib beradi
# print(f"{name} qalesan {name}") stringni ozgartiradi

# list_numbers = [45, 1, 2, 20, 3, 2, 3, 9, 4, 2, 5, 2, 60]
# print(list_numbers.count(2))
# max_number = 0
# for number in list_numbers:
#     print(number)
# print(max_number)

# list_numbers = list(dict.fromkeys(list_numbers))  # listdagi bir xil elementlani ob tashidi
# print(min(list_numbers))  # listdagi kichkina sonni oberadi
# print(max(list_numbers))  # listdagi kotta sonni oberadi

# print(len(list_numbers))
# list_names = []
# list_names.append("Sherzod")
# print(list_names)
# # while True:
#     name = input('Enter name ')

import random

list_numbers = [0, 1, 2, 3, 4, 5, 6]
player1 = False
player2 = False
while player1 != True and player2 != True:
    player_num1 = 0
    player_num2 = 0
    player1_input = input('Are your ready 1 ?')
    if player1_input == "y":
        player_num1 = random.choice(list_numbers)
    player2_input = input('Are your ready 2 ?')
    if player2_input == "y":
        player_num2 = random.choice(list_numbers)
    print('player1', player_num1)
    print('player2', player_num2)
    if player_num1 > player_num2:
        player1 = True

        print('player 1 yutdi')
        break
    elif player_num2 > player_num1:
        player1 = False

        print('player 2 yutdi')
        break
    else:
        print('durrang')

# random_num = random.choice(list_numbers)
# print(random_num)
print("Hello world  2  2")