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
    - X-axis: years
    - Y-axis: life expectancy values
    - Figure size: 16x12 inches
    - Line width: 3 points

    Exceptions that could be raised:
    - TypeError: when data contains non-numeric values for plotting
    - AttributeError: if DataFrame operations fail due to invalid structure

    Dependencies:
    - matplotlib.pyplot: for plotting
    - load_csv.load: for CSV loading with error handling
    """
    df = load(df_path)
    if df is None:
        return
    
    if 'country' not in df.columns:
        print("Dataset error: missing 'country' column")
        return

    df.set_index('country', inplace=True)

    if country not in df.index:
        print(f'Dataset error: no data found for country: {country}')
        return
    
    if not all(col.isdigit() for col in df.columns):
        print("Dataset error: year columns are not all integers")
        return

    x_years = df.columns.values.astype(int)
    y_life_expect = df.loc[country].to_numpy()

    plt.figure(figsize=(16, 12))
    plt.plot(x_years,
             y_life_expect,
             linewidth=3,
             label=f'{country} life expectancy projection')
    plt.ylabel('Life expectancy')
    plt.xlabel('Years')
    plt.show()    


if __name__ == '__main__':
    show_plot('life_expectancy_years.csv', 'Thailand')
