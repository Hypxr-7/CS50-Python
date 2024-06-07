import pytest
from project import Hangman

@pytest.fixture
def game():
    word_list = ["python"]
    return Hangman(word_list)

def test_initialization(game):
    assert game._word == "python"
    assert game._guessed_letters == []
    assert game._wrong_guesses == 0
    assert game._guessed_word == "______"
    assert not game._won
    assert not game._lost

def test_handle_guess_correct(game):
    game._handle_guess('p')
    assert game._guessed_word == 'p_____'
    assert game._wrong_guesses == 0
    assert game._guessed_letters == []

def test_handle_guess_incorrect(game):
    game._handle_guess('z')
    assert game._guessed_word == '______'
    assert game._wrong_guesses == 1
    assert 'z' in game._guessed_letters

def test_check_win(game):
    game._guessed_word = "python"
    assert game._check_win() == True
    assert game._won == False

def test_check_loss(game):
    game._wrong_guesses = len(game._hangman_art) - 1
    assert game._check_loss() == True
    assert game._lost == False

def test_multiple_correct_guesses(game):
    game._handle_guess('p')
    game._handle_guess('y')
    game._handle_guess('t')
    assert game._guessed_word == 'pyt___'
    assert game._wrong_guesses == 0

def test_multiple_incorrect_guesses(game):
    game._handle_guess('a')
    game._handle_guess('b')
    game._handle_guess('c')
    assert game._guessed_word == '______'
    assert game._wrong_guesses == 3

def test_mixed_guesses(game):
    game._handle_guess('p')
    game._handle_guess('x')
    game._handle_guess('y')
    game._handle_guess('z')
    assert game._guessed_word == 'py____'
    assert game._wrong_guesses == 2

if __name__ == "__main__":
    pytest.main()
