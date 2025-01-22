def ft_filter(function, iterable):
    """
    Filters elements from the iterable for which the function returns True

    Parameters:
    - function (callable or None): a function that determines which
    elements to include, if None, includes elements that are True
    - iterable: the collection of items to filter

    Returns:
    - iterator: an iterator over the filtered elements
    """
    if function is None:
        return iter([item for item in iterable if item])
    return iter([item for item in iterable if function(item)])
