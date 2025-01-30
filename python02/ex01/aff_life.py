import matplotlib.pyplot as plt
from load_csv import load


def show_plot(df_path: str, country: str) -> None:
    """
    Creates and displays a line plot showing life expectancy projection
    for a specified country

    Parameters:
    - df_path (str): path to the CSV file containing life expectancy data
    - country (str): name of the country to visualize data for

    Returns:
    - None: function displays the plot and doesn't return any value

    Plot details:
    - X-axis: Years
    - Y-axis: Life expectancy values
    - Title: Automatically generated using country name

    Exceptions handled:
    - KeyError: when the specified country is not found in the dataset
    - Any exceptions from load_csv.load function

    Dependencies:
    - matplotlib.pyplot: for plotting
    - load_csv.load: for loading the CSV file
    """
    df = load(df_path)
    if df is None:
        return

    df.set_index('country', inplace=True)
    try:
        df.loc[country]
    except KeyError:
        print(f'No data found for country: {country}')
        return

    x_years = df.columns.values.astype(int)
    y_life_expect = df.loc[country].to_numpy()

    plt.plot(x_years, y_life_expect,
             label=f'{country} life expectancy projection')
    plt.ylabel('Life expectancy')
    plt.xlabel('Years')
    plt.show()


def main():
    show_plot('life_expectancy_years.csv', 'Thailand')


if __name__ == '__main__':
    main()
