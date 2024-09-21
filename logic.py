import random

def place_bet(current_capital):
    while True:
        try:
            bet = int(input(f"У вас {current_capital}$. Введите вашу ставку: "))
            if bet > current_capital or bet <= 0:
                print(f"Ваша ставка должна быть от 1 до {current_capital}$")
            else:
                return bet
        except ValueError:
            print("Введите корректное целое число")

def play_round(secret_number, min_number, max_number):
    while True:
        try:
            guess = int(input(f"Угадайте число от {min_number} до {max_number}: "))
            if guess < min_number or guess > max_number:
                print(f"Число должно быть в диапазоне от {min_number} до {max_number}")
            else:
                return guess == secret_number
        except ValueError:
            print("Введите корректное число")
