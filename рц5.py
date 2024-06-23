import random

class GuessNumberGame:
    def __init__(self, min_number, max_number, max_attempts, initial_capital):
        self.min_number = min_number
        self.max_number = max_number
        self.max_attempts = max_attempts
        self.initial_capital = initial_capital
        self.capital = initial_capital
        self.attempts_left = max_attempts
        self.secret_number = random.randint(min_number, max_number)
        self.current_bet = 1

    def play(self):
        print(f"Добро пожаловать в игру 'Угадай число'!\nУ вас на старте {self.initial_capital} у.е.")

        while self.attempts_left > 0:
            print(f"\nПопытка №{self.max_attempts - self.attempts_left + 1}")
            print(f"У вас на счету {self.capital} у.е.")

            guess = self.get_player_input()

            if guess == self.secret_number:
                self.handle_win()
                break
            else:
                self.handle_loss()
                self.attempts_left -= 1

            if self.attempts_left == 0:
                print(f"\nИгра окончена. Загаданное число было {self.secret_number}.")
                print(f"Ваш финальный капитал: {self.capital} у.е.")
                break

    def get_player_input(self):
        while True:
            try:
                guess = int(input(f"Введите число от {self.min_number} до {self.max_number}: "))
                if self.min_number <= guess <= self.max_number:
                    return guess
                else:
                    print(f"Число должно быть от {self.min_number} до {self.max_number}. Попробуйте еще раз.")
            except ValueError:
                print("Ошибка: введите целое число.")

    def handle_win(self):
        print(f"Поздравляем! Вы угадали число {self.secret_number}.")
        self.capital += self.current_bet
        self.current_bet *= 2

    def handle_loss(self):
        print(f"Неверно. Правильное число было {self.secret_number}.")
        self.capital -= self.current_bet
        self.current_bet = 1

def main():
    min_number = 1
    max_number = 100
    max_attempts = 5
    initial_capital = 100

    game = GuessNumberGame(min_number, max_number, max_attempts, initial_capital)
    game.play()

if __name__ == "__main__":
    main()
