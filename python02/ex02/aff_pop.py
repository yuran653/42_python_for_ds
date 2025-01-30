import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def num_formater(num: int, _) -> str:
    if num >= 1e6:
        return f'{num/1e6:.1f}M'
    elif num >= 1e3:
        return f'{num/1e3:.1f}K'
    return f'{num:.0f}'


def num_string_convert(num: str) -> int:
    num_suffix = {"M": 10**6, "k": 10**3}
    if num[-1] in num_suffix.keys():
        return int(float(num[:-1]) * num_suffix[num[-1]])
    return int(num)


def show_plot(df_path: str, country1: str, country2: str) -> None:
    
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

    vectorized_func = np.vectorize(num_string_convert)
    y_population1 = vectorized_func(y_population1)
    y_population2 = vectorized_func(y_population2)

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
    show_plot('population_total.csv', 'Thailand', 'Russia')
