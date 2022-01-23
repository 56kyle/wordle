
import numpy as np


def get_words(file_name):
    if file_name.endswith('.txt'):
        with open(file_name, 'r') as file:
            return [word.strip('\n') for word in file.readlines()]
    else:
        return np.load(file_name)


def save_words(words: list | np.ndarray, file_name: str):
    if file_name.endswith('.txt'):
        with open(file_name, 'w') as file:
            file.write('\n'.join(words))
    elif file_name.endswith('.npy'):
        np.save(file_name, words)
    else:
        raise ValueError('File name must end with .txt or .npy')
