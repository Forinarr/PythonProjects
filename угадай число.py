import random

random_number = random.randint(1, 5)
user_number = input("Угадай число от 1 до 5: ")
if int(user_number) == random_number:
    print("Ты прав! Загаданное число:", random_number)
else:
    print("Ты НЕ угадал! Загаданное число:", random_number)
