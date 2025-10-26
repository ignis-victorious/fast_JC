#
#  Import LIBRARIES
import os

import pandas as pd

#  Import FILES
# #


def add_student_score(name: str, math_score: int, english_score: int) -> None:
    # Define the new data as a dictionary
    new_data: dict[str, list[str | int]] = {
        "name": [name],
        "math_score": [math_score],
        "english_score": [english_score],
    }

    # Convert the dictionary to a DataFrame
    new_df: pd.DataFrame = pd.DataFrame(data=new_data)

    print(f"Inside Exist {os.path.exists(path='records.csv')}")
    # Check if the file exists
    if os.path.exists(path="records.csv"):
        print(f"Inside Exist {os.path.exists(path='records.csv')}")
        # If the file exists, append the new data without writing the header
        new_df.to_csv(path_or_buf="records.csv", mode="a", header=False, index=False)
    else:
        # If the file doesn't exist, write the new data with the header
        print("Inside Does NOT Exist")
        new_df.to_csv(path_or_buf="records.csv", mode="w", header=True, index=False)
