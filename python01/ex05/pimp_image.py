import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    pass


def ft_red(array: np.ndarray) -> np.ndarray:
    pass


def ft_green(array: np.ndarray) -> np.ndarray:
    pass


def ft_blue(array: np.ndarray) -> np.ndarray:
    pass


def ft_grey(array: np.ndarray) -> np.ndarray:
    return np.dot(array[..., :3], [0.299, 0.587, 0.114])
