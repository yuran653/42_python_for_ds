import numpy as np
import PIL.Image


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the specified path and returns it as a NumPy array

    Parameters:
    - path (str): the file path to the image

    Returns:
    - np.ndarray: a NumPy array representation of the image,
                  or None if an error occurs

    Raises:
    - TypeError: if the provided path is not a string
    - Exception: for any other errors encountered during image loading
    """
    try:
        if path is None:
            raise ValueError("'path' is None")
        if type(path) is not str:
            raise TypeError("'path' must be a string")
        with PIL.Image.open(path) as image:
            np_image = np.array(image)
            print(f'The shape of image is: {np_image.shape}')
            return np_image
    except ValueError as e:
        print(f'ValueError: ft_load(): {e}')
        return None
    except TypeError as e:
        print(f'TypeError: ft_load(): {e}')
        return None
