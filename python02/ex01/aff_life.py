import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def show_plot(df: pd.DataFrame) -> None:
    if df is None:
        pass
    df = load('life_expectancy_years.csv')
    df = df.loc[df['country'] == 'Thailand']
