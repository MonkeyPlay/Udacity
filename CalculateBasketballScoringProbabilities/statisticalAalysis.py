
import pandas as pd

def import_csv(file_path):
    """
    Imports a CSV file using pandas and returns the DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the CSV data.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError as e:
        print(f"Parsing error: {e}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    file_path = "CalculateBasketballScoringProbabilities/stephen_curry_shots_2023.csv"
    df = import_csv(file_path)
    print(df)
    print(df['result'])
    counts = df['result'].value_counts()
    print(counts)


