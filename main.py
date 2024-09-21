from decouple import config
from logic import place_bet, play_round
import random

def main():
    min_number = config('min_number', cast=int)
    max_number = config('max_number', cast=int)
    attempts = config('attempts', cast=int)
    starting_capital = config('starting_capital', cast=int)

    capital = starting_capital

    print("Добро пожаловать в игру 'Угадай число'!")

    secret_number = random.randint(min_number, max_number)

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt} из {attempts}")

        bet = place_bet(capital)

        if play_round(secret_number, min_number, max_number):
            print("Поздравляем! Вы угадали число!")
            capital += bet * 2  
            break
        else:
            print("Неверно! Вы теряете свою ставку.")
            capital -= bet

        if capital <= 0:
            print("У вас закончились деньги. Игра окончена.")
            return

    if capital > 0:
        print(f"Игра завершена. Ваш итоговый капитал: {capital}$")
    else:
        print(f"Вы проиграли. Число было: {secret_number}")

if __name__ == "__main__":
    main()

