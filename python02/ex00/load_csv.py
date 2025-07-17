import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a CSV file into a pandas DataFrame and prints its dimensions

    Parameters:
    - path (str): path to the CSV file to be loaded

    Returns:
    - pd.DataFrame: a pandas DataFrame containing the loaded data,
                    or None if an error occurs during loading

    Exceptions handled:
    - FileNotFoundError: when the specified file path doesn't exist
    - UnicodeDecodeError: when the file encoding is invalid
    - pd.errors.EmptyDataError: when the CSV file is empty
    - pd.errors.ParserError: when CSV parsing fails due to malformed data
    """
    try:
        df = pd.read_csv(path)
        print(f'Loading dataset of dimensions {df.shape}')
        return df
    except FileNotFoundError:
        print(f'File not found: load(): {path}')
        return None
    except UnicodeDecodeError:
        print(f'Invalid file encoding: load(): {path}')
        return None
    except pd.errors.EmptyDataError:
        print(f'Empty dataset: load(): {path}')
        return None
    except pd.errors.ParserError:
        print(f'Parser error: load(): {path}')
        return None
    
if __name__ == "__main__":
    load('life_expectancy_years.csv')
