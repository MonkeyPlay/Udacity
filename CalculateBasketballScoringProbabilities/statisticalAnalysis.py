
from math import comb
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
    #print(df)
    #print(df['result'])
    makes = df['result'].value_counts()
    pointers = df['shot_type'].value_counts()
    total_shots = df['result'].size

    #print(makes / total_shots)
    #print(total_shots)
    #print(pointers / total_shots)

    # Probabilities
    prob_make = makes.iloc[1] / total_shots
    prob_miss = makes.iloc[0] / total_shots
    prob_three_pointer = pointers.iloc[0] / total_shots
    prob_two_pointer = pointers.iloc[1] / total_shots

    # 1. Probability of making 3 of the next 4 shots
    p_make = prob_make
    p_3_of_4 = comb(4, 3) * (p_make**3) * ((1 - p_make)**1)

    # 2. Probability that 4 of the next 5 shots are three-pointers
    p_3pt = prob_three_pointer
    p_4_of_5_3pt = comb(5, 4) * (p_3pt**4) * ((1 - p_3pt)**1)


    print('Total Shots:', total_shots)
    print('Probability of Make (TRUE):', prob_make.round(4))
    print('Probability of Miss (FALSE)', prob_miss.round(4))
    print('Proportion of Three-Pointers', prob_three_pointer.round(4))
    print('Proportion of Two-Pointers', prob_two_pointer.round(4))

    print("-"*40)
    print("Probability of making 3 of next 4 shots", p_3_of_4.round(4))
    print("Probability that 4 of next 5 shots are three-pointers", p_4_of_5_3pt.round(4))


    # Total shots by type
    three_pt_df = df[df['shot_type'] == 3]
    two_pt_df = df[df['shot_type'] == 2]

    # Conditional probabilities for future shots
    # P(Make | 3PT) = Makes among 3PT / Total 3PT
    p_make_given_3pt = three_pt_df['result'].mean().round(4)
    p_lead_given_3pt = three_pt_df['lead'].mean().round(4)

    # P(Make | 2PT) = Makes among 2PT / Total 2PT
    p_make_given_2pt = two_pt_df['result'].mean().round(4)
    p_lead_given_2pt = two_pt_df['lead'].mean().round(4)

    print("-"*40)
    print("P(Make | Three-Pointer)", p_make_given_3pt)
    print("P(Lead | Three-Pointer)", p_lead_given_3pt)
    print("P(Make | Two-Pointer)", p_make_given_2pt)
    print("P(Lead | Two-Pointer)", p_lead_given_2pt)


    # Filter only made shots
    made_df = df[df['result'] == True]
    total_made = made_df['result'].size
    
    # Conditional probabilities given that a shot was made
    p_3pt_given_make = (made_df['shot_type'] == 3).sum() / total_made
    p_2pt_given_make = (made_df['shot_type'] == 2).sum() / total_made
    p_lead_given_make = made_df['lead'].mean().round(4)

    print("-"*40)
    print("P(Three-Pointer | Made Shot)", p_3pt_given_make.round(4))
    print("P(Two-Pointer | Made Shot)", p_2pt_given_make.round(4))
    print("P(Lead | Made Shot)", p_lead_given_make)


