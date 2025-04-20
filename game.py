#1
def calculator():
    expression = input("Введите выражение (например, 2 + 2): ")
    try:
        result = eval(expression)
        print(f"Результат: {result}")
    except:
        print("Ошибка: Неверное выражение.")

calculator()
#2
import random

def guess_number():
    number = random.randint(0, 10)
    attempts = 3
    print("Угадайте число от 0 до 10. У вас 3 попытки.")

    for attempt in range(attempts):
        guess = int(input(f"Попытка {attempt + 1}: "))
        if guess == number:
            print("Поздравляем! Вы угадали!")
            return
        elif guess < number:
            print("Загаданное число больше!")
        else:
            print("Загаданное число меньше!")

    print(f"Вы проиграли. Загаданное число было: {number}")

guess_number()