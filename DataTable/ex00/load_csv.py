import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV dataset from the specified path and return it as a pandas
    DataFrame.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("The file doesn't exist")
        if not path.lower().endswith('.csv'):
            raise AssertionError("The file format is not .csv")
        try:
            df = pd.read_csv(path)
        except pd.errors.EmptyDataError:
            raise AssertionError("The file is empty")
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return None


def main():
    pass


if __name__ == "__main__":
    main()
