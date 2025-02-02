# import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


"""
A program to visualize and compare population trends between two countries
from 1800 to 2050 using data from 'population_total.csv'

The program loads CSV data, processes population values, and creates
a line plot showing population changes over time for two specified countries
"""


def num_formater(num: int, _) -> str:
    """
    Formats large numbers into millions (M) or thousands (K)
    for readable axis labels

    Parameters:
    - num (int): number to format
    - _ : Unused position parameter required by matplotlib formatter

    Returns:
    - str: formatted string with M/K suffix
    """
    if num >= 1e6:
        return f'{num/1e6:.1f}M'
    elif num >= 1e3:
        return f'{num/1e3:.1f}K'
    return f'{num:.0f}'


def num_string_convert(num: str) -> int:
    """
    Converta a string numbers with M/k suffixes to integer values

    Parameters:
    - num (str): number string possibly containing M/k suffix

    Returns:
    - int: converted integer value
    """
    num_suffix = {"M": 10**6, "k": 10**3}
    if num[-1] in num_suffix.keys():
        return int(float(num[:-1]) * num_suffix[num[-1]])
    return int(num)


def show_plot(df_path: str, country1: str, country2: str) -> None:
    """
    Creates and displays a population comparison plot for two countries

    Parameters:
    - df_path (str): path to the CSV file containing population data
    - country1 (str): name of the 1st country to plot
    - country2 (str): name of the 2nd country to plot

    Returns:
    - None: Displays the plot directly
    
    Raises:
    - KeyError: if specified countries are not found in the dataset
    """
    df = load(df_path)
    if df is None:
        return

    df.set_index('country', inplace=True)
    try:
        df.loc[country1]
        df.loc[country2]
    except KeyError as e:
        print(f'No data found for country: {e}')
        return

    x_years = df.columns.values.astype(int)
    y_population1 = df.loc[country1]
    y_population2 = df.loc[country2]

    # vectorized_func = np.vectorize(num_string_convert)
    # y_population1 = vectorized_func(y_population1)
    # y_population2 = vectorized_func(y_population2)

    # For the strict following to the subfect requirements
    # I will use less efficient 'apply' method
    y_population1 = df.loc[country1].apply(num_string_convert)
    y_population2 = df.loc[country2].apply(num_string_convert)

    plt.figure(figsize=(16, 12))
    plt.plot(x_years, y_population1,
             label=country1, 
             linewidth=3,
             color='#2D2A4A')
    plt.plot(x_years, y_population2,
             label=country2,
             linewidth=3,
             color='#D52B1E')
    plt.title(f'Population projection for {country1} and {country2}')
    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.legend()
    plt.xlim(1800,2050)
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(num_formater))
    plt.show()


if __name__ == '__main__':
    show_plot('population_total.csv', 'Thailand', 'South Korea')
