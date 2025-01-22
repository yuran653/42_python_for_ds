def ft_tqdm(lst: range) -> None:
    """
    A custom progress bar generator for iterating over a range of items

    Args:
    - lst (range): The range of items to iterate through.

    Yields:
    - the next item in the provided range.

    Behavior:
    - displays a progress bar in the terminal that updates with each iteration
    - the progress bar includes:
      - percentage of completion
      - a visual bar representation (using filled and empty spaces)
      - current iteration count out of the total
    - progress is updated in-place using '\r' (carriage return)
    """
    total_len = len(lst)
    num_len = len(str(total_len))
    bar_len = 74
    for i, item in enumerate(lst, start=1):
        progress = int((i // total_len) * 100)
        filled_len = int(bar_len * i // total_len)
        bar = '\u2588' * filled_len + '\u0020' * (bar_len - filled_len)
        print(f'\r{progress:>3}%|{bar}| {i:>{num_len}}/{total_len}',
              end='')
        yield item
    print()
