

import numpy as np

from util import get_words, save_words


wordle_word_length = 5


def analyze():
    answers = get_words('../data/wordle_answers.txt')
    guesses = get_words('../data/wordle_guesses.txt')
    save_words(convert_to_numpy_array(answers), '../data/wordle_answers.npy')
    save_words(convert_to_numpy_array(guesses), '../data/wordle_guesses.npy')


def convert_to_numpy_array(words):
    # Converts a list of words into a numpy array where each row is a word.
    # All words in the list are the same length.
    # The array has shape (len(words), len(words[0]))
    return np.array([list(word) for word in words])


if __name__ == '__main__':
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    analyze()


