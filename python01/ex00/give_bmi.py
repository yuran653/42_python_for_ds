import numpy as np
    

def give_bmi(
        height: list[int | float],
        weight: list[int | float]
) -> list[int | float]:
    try:
        if type(height) is not list or type(weight) is not list:
            raise TypeError('Passed arguments must be a list')
        np_heights = np.array(height)
        np_weights = np.array(weight)
        if not np.issubdtype(np_heights.dtype, np.number) or not np.issubdtype(np_weights.dtype, np.number):
            raise TypeError('Passed lists must contain only numeric values')
        if np_heights.size == 0 or np_weights.size == 0 or np_heights.size!= np_weights.size:
            raise ValueError('Passed arrays must be not empty and have equal length')
        return (np_weights / (np_heights ** 2)).tolist()
    except Exception as e:
        print(f'give_bmi(): {e}')
        return None


def apply_limit(
        bmi: list[int | float],
        limit: int
) -> list[bool]:
    try:
        if type(bmi) is not list or type(limit) is not int:
            raise TypeError("'bmi' must be a list and 'limit' must be an integer")
        np_bmi = np.array(bmi)
        if not np.issubdtype(np_bmi.dtype, np.number):
            raise TypeError("'bmi' list must contain only numeric values")
        return (np_bmi > limit).tolist()
    except Exception as e:
        print(f'apply_limit(): {e}')
        return None
