import random

def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def process_bet(guess, actual_number, bet, balance):
    if guess == actual_number:
        print(f"Поздравляем! Вы угадали число {actual_number}. Ваша ставка удваивается!")
        return balance + bet
    else:
        print(f"Неправильно! Загаданное число было {actual_number}. Вы теряете свою ставку")
        return balance - bet
