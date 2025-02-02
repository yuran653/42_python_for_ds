import matplotlib.pyplot as plt
import seaborn as sns
from load_csv import load


def show_plot(year: str) -> None:
    """
    Creates and displays a scatter plot comparing life expectancy
    versus GDP for all countries in a specified year

    Parameters:
    - year (str): the year for which to create the visualization

    Returns:
    - None: displays the plot directly

    Raises:
    - KeyError: if the specified year is not found in the datasets
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

    try:
        year_life = df_life[year]
        year_income = df_income[year]
    except KeyError:
        print(f'No data found for year: {year}')
        return

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
                    c=year_income.index.map(color_map),
                    legend=False)
    plt.title('The projection of life expectancy in relation to the GDP'
              f' of the year {year} for each country')
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life expectancy')
    plt.legend()
    plt.gca().xaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))
    plt.show()


if __name__ == '__main__':
    show_plot('1900')
