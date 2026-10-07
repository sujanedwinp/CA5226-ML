"""
csvinfo.py
Demonstration of converting Dictionaries and Arrays into .csv files in Python.

Covers:
1. Converting a Dictionary to CSV (using Pandas and standard csv module)
2. Converting an Array/List to CSV (using Pandas, standard csv module, and NumPy)
"""

import csv
import os
import pandas as pd
import numpy as np


def demo_dict_to_csv():
    print("=" * 60)
    print("1. CONVERTING A DICTIONARY TO A .CSV FILE")
    print("=" * 60)

    # ---------------------------------------------------------
    # Scenario A: Column-oriented Dictionary (Keys = Column Names, Values = Lists)
    # This is the most common format used with pandas.
    # ---------------------------------------------------------
    data_dict = {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [24, 27, 22, 32],
        "Score": [88.5, 92.0, 79.5, 95.0]
    }

    # Method 1A: Using Pandas (Recommended)
    df_from_dict = pd.DataFrame(data_dict)
    pandas_dict_csv_file = "output_dict_pandas.csv"
    # index=False avoids writing row index numbers (0, 1, 2...) into the CSV
    df_from_dict.to_csv(pandas_dict_csv_file, index=False)
    print(f"[Pandas] Dict converted and saved to '{pandas_dict_csv_file}':\n")
    print(df_from_dict)
    print()

    # Method 1B: Using Python's built-in 'csv' module (Standard Library)
    builtin_dict_csv_file = "output_dict_builtin.csv"
    with open(builtin_dict_csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write column headers
        headers = list(data_dict.keys())
        writer.writerow(headers)
        # Write rows (transpose columns into rows)
        num_rows = len(next(iter(data_dict.values())))
        for i in range(num_rows):
            row = [data_dict[col][i] for col in headers]
            writer.writerow(row)
    print(f"[Built-in csv] Column-dict saved to '{builtin_dict_csv_file}'\n")

    # ---------------------------------------------------------
    # Scenario B: Row-oriented List of Dictionaries
    # ---------------------------------------------------------
    list_of_dicts = [
        {"Name": "Alice", "Age": 24, "Score": 88.5},
        {"Name": "Bob", "Age": 27, "Score": 92.0},
        {"Name": "Charlie", "Age": 22, "Score": 79.5},
        {"Name": "David", "Age": 32, "Score": 95.0}
    ]

    # Using csv.DictWriter
    dictwriter_file = "output_list_of_dicts.csv"
    with open(dictwriter_file, mode="w", newline="") as file:
        fieldnames = ["Name", "Age", "Score"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list_of_dicts)
    print(f"[csv.DictWriter] List of dicts saved to '{dictwriter_file}'\n")


def demo_array_to_csv():
    print("=" * 60)
    print("2. CONVERTING AN ARRAY / LIST TO A .CSV FILE")
    print("=" * 60)

    # 2D Array / Nested List data
    array_data = [
        [1, "Alice", 88.5],
        [2, "Bob", 92.0],
        [3, "Charlie", 79.5],
        [4, "David", 95.0]
    ]
    columns = ["ID", "Name", "Score"]

    # Method 2A: Using Pandas (Recommended)
    df_from_array = pd.DataFrame(array_data, columns=columns)
    pandas_array_csv_file = "output_array_pandas.csv"
    df_from_array.to_csv(pandas_array_csv_file, index=False)
    print(f"[Pandas] Array converted and saved to '{pandas_array_csv_file}':\n")
    print(df_from_array)
    print()

    # Method 2B: Using Python's built-in 'csv' module
    builtin_array_csv_file = "output_array_builtin.csv"
    with open(builtin_array_csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(columns)       # Write header
        writer.writerows(array_data)   # Write data rows
    print(f"[Built-in csv] Array saved to '{builtin_array_csv_file}'\n")

    # Method 2C: Using NumPy (savetxt) for numeric 2D arrays
    numeric_array = np.array([
        [1.0, 35.0],
        [2.0, 40.0],
        [3.0, 45.0],
        [4.0, 50.0]
    ])
    numpy_csv_file = "output_array_numpy.csv"
    np.savetxt(
        numpy_csv_file,
        numeric_array,
        delimiter=",",
        header="StudyHours,Marks",
        comments="",
        fmt="%.1f"
    )
    print(f"[NumPy] Numeric array saved to '{numpy_csv_file}'\n")


def show_csv_file_contents(filename):
    print(f"--- File preview: {filename} ---")
    with open(filename, mode="r") as f:
        print(f.read())


if __name__ == "__main__":
    demo_dict_to_csv()
    demo_array_to_csv()

    print("=" * 60)
    print("VERIFYING GENERATED CSV CONTENTS")
    print("=" * 60)
    show_csv_file_contents("output_dict_pandas.csv")
    show_csv_file_contents("output_array_pandas.csv")

    # Clean up generated sample files to keep the directory clean
    sample_files = [
        "output_dict_pandas.csv",
        "output_dict_builtin.csv",
        "output_list_of_dicts.csv",
        "output_array_pandas.csv",
        "output_array_builtin.csv",
        "output_array_numpy.csv"
    ]
    for sample_file in sample_files:
        if os.path.exists(sample_file):
            os.remove(sample_file)
    print("Cleaned up sample CSV output files successfully.")
