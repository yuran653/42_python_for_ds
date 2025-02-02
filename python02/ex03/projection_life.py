import pandas as pd
from load_csv import load



def show_plot() -> None:
    df_income = load(
        'income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    df_life = load('life_expectancy_years.csv')
    if df_income is None or df_life is None:
        return
    
    df_income.set_index('country', inplace=True)
    df_life.set_index('country', inplace=True)

    df_income.columns = df_income.columns.astype(int)
    df_life.columns = df_life.columns.astype(int)

    life_drop_columns = list(range(2051, 2101))
    df_life.drop(columns=life_drop_columns, axis=1, inplace=True)

    life_rows_with_nan = df_life[df_life.isna().any(axis=1)]
    income_rows_with_nan = df_income[df_income.isna().any(axis=1)]

    life_rows_with_nan = life_rows_with_nan.index.tolist()
    income_rows_with_nan = income_rows_with_nan.index.tolist()

    countries_to_drop = life_rows_with_nan + income_rows_with_nan

    df_life.drop(countries_to_drop, axis=0, inplace=True)
    df_income.drop(countries_to_drop, axis=0, inplace=True)

    print(df_income.shape)
    print(df_life.shape)


if __name__ == '__main__':
    show_plot()
