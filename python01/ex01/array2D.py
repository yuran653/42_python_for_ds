import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a given list between the specified start and end indices,
    and providing the shape information of the original and sliced data

    Parameters:
    - family (list): the list to slice
    - start (int): the starting index of the slice
    - end (int): the ending index of the slice

    Returns:
    - list: the sliced portion of the input list as a new list
            or None if input validation fails or an exception occurs

    Raises:
    - TypeError: if 'family' is not a list or 'start'/'end' are not integers.
    """
    try:
        if type(family) is not list:
            raise TypeError("'family' must be a list")
        if type(start) is not int or type(end) is not int:
            raise TypeError("'start' and 'end' must be integers")
        np_family = np.array(family)
        print(f'My shape is : {np_family.shape}')
        sliced_np_family = np_family[start:end]
        print(f'My new shape is : {sliced_np_family.shape}')
        return sliced_np_family.tolist()
    except TypeError as e:
        print(f'TypeError: slice_me(): {e}')
        return None
