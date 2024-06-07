# Hangman

## Video Demo:  <https://youtu.be/FU87PiU9Qc0>

## Description:

Hangman is a classic word-guessing game where one player thinks of a word and the other player tries to guess it by suggesting letters within a certain number of guesses. This repository contains a Python implementation of the Hangman game.

### Hangman Class:

The Hangman class represents the game logic and provides methods to play the game.

#### Constructor:

```def __init__(self, word_list)```

#### Parameters:

Contains a single parameter `word_list` that will contain a list of words from which our word that we will guess will be picked from.

#### Attributes:

- `_word` The secret word to be guessed.
- `_guessed_letters` A list to store the letters guessed by the player.
- `_wrong_guesses` An integer to count the number of wrong guesses made by the player.
- `_guessed_word` A string representing the current state of the guessed word, with underscores for unguessed letters.
- `_won` A boolean indicating whether the game has been won.
- `_lost` A boolean indicating whether the game has been lost.
- `_hangman_art` A list of ASCII art representing the hangman's state for each wrong guess.

#### Methods
- `play(self)` Starts the game loop and allows the player to play the game.
- `_draw(self)` Draws the current state of the hangman, guessed letters the guessed word.
- `_check_valid_letter(self)` Prompts the player to enter a letter and validates the input.
- `_handle_guess(self, guess)` Handles the player's guess by updating the guessed word and wrong guesses.
- `_check_win(self)` Checks if the player has won the game.
- `_check_loss(self)` Checks if the player has lost the game

## Usage:

To play the Hangman game, create an instance of the Hangman class with a list of words and call the `play()` method
```
words = ["computer", "gaming", "learning", "python"]
game = Hangman(words)
game.play()
```

## Unit Tests:

- Initialization: `test_initialization` checks if the class is correctly initialized with a word from the list.
- Correct Guess Handling: `test_handle_guess_correct` ensures the guessed word is updated correctly when a correct letter is guessed.
- Incorrect Guess Handling: `test_handle_guess_incorrect` checks if wrong guesses are handled correctly.
- Win Condition: `test_check_win` verifies if the game correctly identifies a win.
- Loss Condition: `test_check_loss` ensures the game identifies a loss correctly.
- Multiple Guesses: Additional tests check multiple correct and incorrect guesses.

## Additional Notes:

- Another way to generate a word list coulf be to use a text file containing multiple words and read that file to make a word list.
- Initially, I did not clear the screen. However, as I tested my program, having a cluttered command line made it slightly annoying, so I googled it and found out you can use `os.system("clear")` on Linux to clear the terminal
- Another problem I noticed was that I would keep forgetting which letters have already been guessed. To resolve this I added a new variable `_guessed_letters` to keep track of them.
- Special thanks to [crishorton](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c) for ASCII artwork of hangman
