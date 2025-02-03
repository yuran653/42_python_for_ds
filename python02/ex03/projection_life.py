import matplotlib.pyplot as plt
import seaborn as sns
from load_csv import load


def num_string_convert(num: any) -> int:
    """
    Converts a string numbers with M/k suffixes to integer values

    Parameters:
    - num (str): number string possibly containing M/k suffix

    Returns:
    - int: converted integer value
    """
    if isinstance(num, int):
        return num

    num_suffix = {"M": 10**6, "k": 10**3}
    if num[-1] in num_suffix.keys():
        return int(float(num[:-1]) * num_suffix[num[-1]])

    return int(num)


def show_plot(year: str) -> None:
    """
    Creates and displays a scatter plot showing life expectancy vs GDP
    for all countries in a specified year

    Parameters:
    - year (str): target year to visualize data for (format: 'YYYY')

    Returns:
    - None: function displays the plot and doesn't return any value

    Plot details:
    - X-axis: Gross Domestic Product (converted to 'k' notation for thousands)
    - Y-axis: Life expectancy values
    - Figure size: 16x12 inches
    - Color mapping: Unique color per country using 'dark:salmon_r' palette
    - Legend: Explicitly disabled

    Exceptions that could be raised:
    - TypeError: if GDP conversion fails due to non-numeric values

    Dependencies:
    - matplotlib.pyplot: for plot configuration and display
    - seaborn: for scatter plot visualization
    - load_csv.load: for data loading from CSV files
    """
    df_income = load(
        'income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    df_life = load('life_expectancy_years.csv')
    if df_income is None or df_life is None:
        return

    df_income.set_index('country', inplace=True)
    df_life.set_index('country', inplace=True)

    if df_income.index.equals(df_life.index) is False:
        print('Countries in datasets do not match')
        return

    if year not in df_income or year not in df_life:
        print(f'No data found for year: {year}')
        return

    year_life = df_life[year]
    year_income = df_income[year].apply(num_string_convert)

    life_rows_with_nan = year_life[year_life.isna()]
    income_rows_with_nan = year_income[year_income.isna()]

    life_rows_with_nan = life_rows_with_nan.index.tolist()
    income_rows_with_nan = income_rows_with_nan.index.tolist()

    countries_to_drop = life_rows_with_nan + income_rows_with_nan

    year_life.drop(countries_to_drop, axis=0, inplace=True)
    year_income.drop(countries_to_drop, axis=0, inplace=True)

    pallete = 'dark:salmon_r'
    color_labels = year_income.index.unique()
    rgb_values = sns.color_palette(pallete, len(color_labels))
    color_map = dict(zip(color_labels, rgb_values))

    plt.figure(figsize=(16, 12))
    sns.scatterplot(x=year_income,
                    y=year_life,
                    hue=color_labels,
                    palette=color_map,
                    legend=False)
    plt.title('The projection of life expectancy in relation to the GDP'
              f' of the year {year} for each country')
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life expectancy')
    plt.gca().xaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: f'{int(x/(1000))}k'))
    plt.show()


if __name__ == '__main__':
    show_plot('1900')
