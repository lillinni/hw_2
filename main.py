from decouple import config
from logic import generate_random_number, process_bet

def main():
    min_num = config('min_number', cast=int)
    max_num = config('max_number', cast=int)
    attempts = config('attempts', cast=int)
    balance = config('initial_balance', cast=int)

    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Вам нужно угадать число от {min_num} до {max_num}.")
    print(f"У вас {attempts} попыток и {balance} начальных очков капитала\n")

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt} из {attempts}. Ваш текущий баланс: {balance}")

        try:
            bet = int(input(f"Введите ставку (не больше вашего баланса: {balance}): "))
            if bet > balance or bet <= 0:
                print("Некорректная ставка. Попробуйте снова")
                continue
        except ValueError:
            print("Ошибка ввода! Введите целое число")
            continue

        try:
            guess = int(input(f"Угадайте число от {min_num} до {max_num}: "))
            if guess < min_num or guess > max_num:
                print(f"Число должно быть в диапазоне от {min_num} до {max_num}")
                continue
        except ValueError:
            print("Ошибка ввода! Введите целое число")
            continue

        actual_number = generate_random_number(min_num, max_num)
        balance = process_bet(guess, actual_number, bet, balance)

        if balance <= 0:
            print("Ваш баланс исчерпан. Игра окончена")
            break

    print(f"\nИгра завершена! Ваш итоговый баланс: {balance}")

if __name__ == "__main__":
    main()

