import numpy as np
import PIL.Image


def zoom(np_image: np.ndarray) -> np.ndarray:
    try:
        if np_image is None:
            raise ValueError("Image is None")
        if len(np_image.shape) != 3:
            raise ValueError("Image must be a 3D array")
        if np_image.shape[2] != 3:
            raise ValueError("Image must have 3 channels (RGB)")
    except Exception as e:
        print(f'zoom(): {e}')
        return None