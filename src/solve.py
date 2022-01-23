

import numpy as np


def load_wordle(path: str):
    return np.load(path)


def save_wordle(path: str, board: np.ndarray):
    np.save(path, board)


def solve_wordle(board: np.ndarray):
    pass


if __name__ == "__main__":
    pass



