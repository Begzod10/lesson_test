import random

# name = "Python"  # -> String
# number = 14  # -> Integer
# number2 = 10.5  # -> Float
#
# person1 = {
#     "name": "John",  # -> Object
#     "age": 25
# }
# True, False -> boolean
# print(list_numbers)


# if number == 12:
#     print(True)
# elif number == 13:
#     print("13 ga teng")
# else:
#     print(False)

# get_name = input("Enter your name ")
# print("Hello " + get_name)
# print(f"Hello  {get_name}")  # formatted strings

# current_year = 2022
# get_year = int(input("Enter your born year "))
# result = current_year - get_year
# print(f"Your age is {result}")

# lower(), upper(), capitalize()

# letter = "begzod is programmer"
# new_letter = letter.replace("begzod", "ulug'")

# new_letter = letter.find("i")
# new_letter = len(letter)
# print(new_letter)

# for num in list_numbers:
#
#     # if num == 45:
#     #     break
#     if num == 45:
#         continue
#     print(num)

# list_numbers.sort()
# list_numbers = list(dict.fromkeys(list_numbers))
# new_numbers = []
#
# for num in list_numbers:
#     if num not in new_numbers:
#         new_numbers.append(num)
# print(list_numbers)
# print(new_numbers)
# print(len(list_numbers))
list_products = []

# while True:
#     number = input('enter product ')
#     list_products.append(number)
#     print(list_products)
#     if len(list_products) == 10:
#         break
# for num in list_numbers:
#     if num == 20:
#         break
#     print(num)
# list_numbers.sort()
# print(list_numbers)
# new_list = []
# for num in list_numbers:
#     if num not in new_list:
#         new_list.append(num)
#
# print(new_list)
#
# list_numbers = list(dict.fromkeys(list_numbers))
# print(list_numbers)
# max_num = 0
# list_numbers = [45, 1, 2, 20, 2, 3, 9, 4, 2, 5, 2, 60]  # -> list
# # max number
# for num in list_numbers:
#     if max_num > num:
#         max_num = num
#
# print(max_num)
# max_num = min(list_numbers)
# print(max_num)
# secret_number = 8
# guess_number = 0
# while True:
#     number = int(input('Enter number '))
#     if secret_number == number:
#         print('You win!!!')
#         break
#     else:
#         print('topomadin')
#
# while guess_number != secret_number:
#     number = int(input('Enter number '))
#     guess_number = number
#     if guess_number != secret_number:
#         print('you failed !!!')
# else:
#     print('You win !!!')

# for num in range(9):
#     for num2 in range(4):
#         print(f"num1: {num} num2: {num2}")


numbers = [1, 2, 3, 4, 5, 6, 2]

# print(list_number[0][0])
# list_number.append(2)
# list_number.insert(4, 10)
# if 19 in list_number:
#     list_number.remove(19)
# list_number.pop()

# list_number.clear()
# print(numbers.index(2))
# print(numbers.count(2))
# numbers.sort()
# numbers.reverse()

# number2 = numbers.copy()
# numbers.append(23)
# print(number2)
# print(numbers)

# random_number = random.choice(numbers)
# print(random_number)
# nick = "tente"
# text = f"Sherzod {nick}"
# print(text)


# list_numbers = [0, 1, 2, 3, 4, 5, 6]
# player1_turn = False
# player2_turn = False
# player1_number = 0
# player2_number = 0
#
# while player1_turn != True and player2_turn != True:
#     player1 = input('Are your ready player1 ? ')
#     player2 = input('Are your ready player2 ? ')
#     if player1 == "yes" and player2 == "yes":
#         player1_number = random.choice(list_numbers)
#         player2_number = random.choice(list_numbers)
#         if player1_number > player2_number:
#             print(f"Player1 yutdi player1: {player1_number} player2: {player2_number}")
#             player1_turn = True
#         elif player1_number < player2_number:
#             print(f"Player2 yutdi player1: {player1_number} player2: {player2_number}")
#             player2_turn = True
#         else:
#             print(f"Draw player1: {player1_number} player2: {player2_number}")
#             player1_turn = False
#             player2_turn = False
# ball = 0
# overall_ball = 15
# while player1_turn != False or player2_turn != False:
#     if player1_turn:
#         player1 = input('Are your ready player1 ? ')
#         player1_number = random.choice(list_numbers)
#         print(f'Player1 {player1_number}')
#         if player1_number != 0:
#             ball += player1_number
#             print(f'Umumiy ball: {ball}')
#             if ball >= overall_ball:
#                 print(f"Player1 yutdi {ball}")
#                 break
#         else:
#             player1_turn = False
#             player2_turn = True
#             print(f'Player1 : {player1_number} oldi')
#             ball = 0
#     else:
#         player2 = input('Are your ready player2 ? ')
#         player2_number = random.choice(list_numbers)
#         print(f'Player2 {player2_number}')
#         if player2_number != 0:
#             ball += player2_number
#             print(f'Umumiy ball: {ball}')
#             if ball >= overall_ball:
#                 print(f"Player2 yutdi {ball}")
#                 break
#         else:
#             player2_turn = False
#             player1_turn = True
#             ball = 0
#             print(f'Player2 : {player2_number} oldi')


# dictionary = [
#     {
#         "hello": "salom",
#         "bye": "xayr"
#     }
# ]
#
#
# word = input('Enter word ')
# for item in dictionary:
#
#     if item.get(word):
#         print(item.get(word))


# def say_hello(name, age, surname):
#     print(f'Hello {name} age:{age} surname:{surname}')
#
#
# say_hello(surname="Mirhamidov", name="Behruz", age=14)
#
# try:
#     number = int(input('number-1 '))
#     number2 = int(input('number-2 '))
#
#     print(number / number2)
# except ZeroDivisionError:
#     print("sonni 0ga bolib bomidi")
# except ValueError:
#     print('son kiritilmagan')


number = 20


# def change_number():
#     global number
#     number = 30
#     return number
#
#
# print(change_number())
# print(number)

# def change_number():
#     number = 10
#
#     def inner_func():
#         nonlocal number
#         number = 20
#
#     inner_func()
#     print(number)
#
#
# change_number()

#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def fikrlidi(self, age):
#         print(f'{self.name} {age} fikrlidi')
#
#     # def sakridi(self):
#
#
# class Person2(Person):
#
#     def talk(self):
#         print(f'{self.name} can talk')
#
#     pass


# sherzod = Person('Sherzod')
# sherzod.fikrlidi(14)
#
# person = Person('Person')
# print(person.name)
# person2 = Person2("Sherzod")
# person2.
def hello():
    print('Hello')


from darslik.app import *

person = Person("Begzod")

person.hello()
person.run("Jumaniyozov")
