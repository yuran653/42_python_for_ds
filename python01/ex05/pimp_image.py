import numpy as np
import PIL


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of an image by subtracting each pixel value from 255
    
    Parameters:
    - array (np.ndarray): input image array of shape (height, width, channels)
                          with values in range [0, 255]
    
    Returns:
    - np.ndarray: inverted image array of same shape as input, or None if error
    """
    # Allowed operators for the function: =, +, -, *
    inverted_array = 255 - array
    print(f'The shape of image is: {inverted_array.shape}')
    if inverted_array.shape != array.shape:
        return None
    inverted_array = inverted_array.astype(np.uint8)
    print(inverted_array)
    return inverted_array



def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Isolates the red channel of an image by setting green and blue channels to zero
    
    Parameters:
    - array (np.ndarray): input image array of shape (height, width, channels)
                          with values in range [0, 255]
    
    Returns:
    - np.ndarray: red channel isolated image array of same shape as input, 
                  or None if error
    """
    # Allowed operators for the function: =, *
    red_array = array.copy()
    red_array[:, :, 1] *= 0
    red_array[:, :, 2] *= 0
    print(f'The shape of image is: {red_array.shape}')
    if red_array.shape != array.shape:
        return None
    red_array = red_array.astype(np.uint8)
    print(red_array)
    return red_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Isolates the green channel of an image by setting red and blue channels to zero
    
    Parameters:
    - array (np.ndarray): input image array of shape (height, width, channels)
                          with values in range [0, 255]
    
    Returns:
    - np.ndarray: green channel isolated image array of same shape as input,
                  or None if error
    """
    # Allowed operators for the function: =, -
    green_array = array.copy()
    green_array[:, :, 0] -= array[:, :, 0]
    green_array[:, :, 2] -= array[:, :, 2]
    print(f'The shape of image is: {green_array.shape}')
    if green_array.shape != array.shape:
        return None
    green_array = green_array.astype(np.uint8)
    print(green_array)
    return green_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Isolates the blue channel of an image by setting red and green channels to zero
    
    Parameters:
    - array (np.ndarray): input image array of shape (height, width, channels)
                          with values in range [0, 255]
    
    Returns:
    - np.ndarray: blue channel isolated image array of same shape as input,
                  or None if error
    """
    # Allowed operators for the function: =
    blue_array = array.copy()
    blue_array[:, :, 0] = 0
    blue_array[:, :, 1] = 0
    print(f'The shape of image is: {blue_array.shape}')
    if blue_array.shape != array.shape:
        return None
    blue_array = blue_array.astype(np.uint8)
    print(blue_array)
    return blue_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts an RGB image to grayscale by averaging the color channels.
    
    Parameters:
    - array (np.ndarray): input image array of shape (height, width, channels)
                          with values in range [0, 255]
    
    Returns:
    - np.ndarray: grayscale image array of same shape as input, or None if error
    """
    # Allowed operators for the function: =, /
    mean_array = np.mean(array, axis=2)
    gray_array = np.zeros_like(array)
    gray_array[:, :, :] = mean_array[:, :, np.newaxis]
    print(f'The shape of image is: {gray_array.shape}')
    if gray_array.shape != array.shape:
        return None
    gray_array = gray_array.astype(np.uint8)
    print(gray_array)
    return gray_array
