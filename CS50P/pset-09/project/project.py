import random
import os

class Hangman:
    def __init__(self, word_list):
        self._word = (random.choice(word_list)).lower()
        self._guessed_letters = []
        self._wrong_guesses = 0
        self._guessed_word = "_" * len(self._word)
        self._won = False
        self._lost = False

        self._hangman_art =    [" +---+\n"
                                " |   |\n"
                                "     |\n"
                                "     |\n"
                                "     |\n"
                                "     |\n"
                                "==========",
                                " +---+\n"
                                " |   |\n"
                                " O   |\n"
                                "     |\n"
                                "     |\n"
                                "     |\n"
                                "==========",
                                " +---+\n"
                                " |   |\n"
                                " O   |\n"
                                " |   |\n"
                                "     |\n"
                                "     |\n"
                                "==========",
                                " +---+\n"
                                " |   |\n"
                                " O   |\n"
                                "/|   |\n"
                                "     |\n"
                                "     |\n"
                                "==========",
                                " +---+\n"
                                " |   |\n"
                                " O   |\n"
                                "/|\\  |\n"
                                "     |\n"
                                "     |\n"
                                "==========",
                                " +---+\n"
                                " |   |\n"
                                " O   |\n"
                                "/|\\  |\n"
                                "/    |\n"
                                "     |\n"
                                "==========",
                                " +---+\n"
                                " |   |\n"
                                " O   |\n"
                                "/|\\  |\n"
                                "/ \\  |\n"
                                "     |\n"
                                "=========="]


    def play(self):
        while(not self._won and not self._lost):
            os.system("clear")
            self._draw()
            self._handle_guess(self._check_valid_letter())
            self._won = self._check_win()
            self._lost = self._check_loss()


    def _draw(self):
        print(self._hangman_art[self._wrong_guesses])
        print(self._guessed_word)
        print("Guesses Letters: ", self._guessed_letters)


    def _check_valid_letter(self):
        letter = input("Enter a Letter: ")
        while (True):
            if len(letter) == 1 and letter.isalpha():
                return letter.lower()
            else:
                letter = input("Invalid input. Please enter a lowercase letter: ")


    def _handle_guess(self, guess):
        if guess in self._word:
            for i, letter in enumerate(self._word):
                if letter == guess:
                        self._guessed_word = self._guessed_word[:i] + guess + self._guessed_word[i+1:]
        else:
            self._wrong_guesses += 1
            self._guessed_letters.append(guess)


    def _check_win(self):
        if self._word != self._guessed_word:
            return False
        os.system("clear")
        print(self._hangman_art[self._wrong_guesses])
        print(self._guessed_word)
        print("You win! The word was", self._word)
        return True


    def _check_loss(self):
        if self._wrong_guesses < 6:
            return False
        os.system("clear")
        print(self._hangman_art[self._wrong_guesses])
        print(self._guessed_word)
        print("You lost! The word was", self._word)
        return True


def main():
    words = ["computer", "gaming", "learning", "python", "hello"]

    game = Hangman(words)
    game.play()


if __name__ == "__main__":
    main()



