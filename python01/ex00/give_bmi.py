import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
) -> list[int | float]:
    """
    Calculate BMI values for given heights and weights

    Parameters:
    - height (list[int | float]): list of heights in meters
    - weight (list[int | float]): list of weights in kilograms

    Returns:
    - list[int | float]: list of BMI values corresponding to height and weight
                         or None if an error occurs

    Raises:
    - TypeError: if height or weight is not a list
                 or contains non-numeric values
    - ValueError: if height or weight lists are empty or of unequal length
    """
    try:
        if type(height) is not list or type(weight) is not list:
            raise TypeError('Passed arguments must be a list')
        np_heights = np.array(height)
        np_weights = np.array(weight)
        if not np.issubdtype(np_heights.dtype, np.number) or \
                not np.issubdtype(np_weights.dtype, np.number):
            raise TypeError(
                'Passed lists must contain only numeric values')
        if np_heights.size == 0 or np_weights.size == 0 or \
                np_heights.size != np_weights.size:
            raise ValueError(
                'Passed arrays must be not empty and have equal length')
        return (np_weights / (np_heights ** 2)).tolist()
    except TypeError as e:
        print(f'TypeError: give_bmi(): {e}')
        return None
    except ValueError as e:
        print(f'ValueError: give_bmi(): {e}')
        return None


def apply_limit(
        bmi: list[int | float],
        limit: int
) -> list[bool]:
    """
    Apply a limit to a list of BMI values and return a list of booleans

    Parameters:
    - bmi (list[int | float]): list of BMI values
    - limit (int): integer limit to compare against BMI values

    Returns:
    - list[bool]: list where each element is True if BMI > limit, else False
                  or None if an error occurs

    Raises:
    - TypeError: if bmi is not a list, limit is not an integer,
                 or bmi contains non-numeric values
    """
    try:
        if type(bmi) is not list or type(limit) is not int:
            raise TypeError(
                "'bmi' must be a list and 'limit' must be an integer")
        np_bmi = np.array(bmi)
        if not np.issubdtype(np_bmi.dtype, np.number):
            raise TypeError("'bmi' list must contain only numeric values")
        return (np_bmi > limit).tolist()
    except TypeError as e:
        print(f'TypeError: apply_limit(): {e}')
        return None
