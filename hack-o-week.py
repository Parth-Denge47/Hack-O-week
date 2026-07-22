

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


filename = r"C:\Users\sit.lab5.SIT-CDC0\Desktop\do not open\fifa_world_cup_2026_player_performance.csv"


def load_data(file):
    df = pd.read_csv(file, engine="python", on_bad_lines="skip")
    return df


class FIFAAnalysis:

    def __init__(self, dataframe):
        self.df = dataframe

    
    def dataset_info(self):

        print("\n========== FIRST 5 ROWS ==========")
        print(self.df.head())

        print("\n========== DATASET INFO ==========")
        self.df.info()

        print("\n========== MISSING VALUES ==========")
        print(self.df.isnull().sum())

    
    def clean_data(self):

        print("\n========== DATA CLEANING ==========")

        for col in self.df.columns:

           
            if self.df[col].isnull().sum() == 0:
                continue

            
            if pd.api.types.is_numeric_dtype(self.df[col]):

                mean_value = self.df[col].mean()
                self.df[col] = self.df[col].fillna(mean_value)

            
            else:

                if not self.df[col].mode().empty:
                    mode_value = self.df[col].mode()[0]
                    self.df[col] = self.df[col].fillna(mode_value)

        print("\nMissing Values After Cleaning")
        print(self.df.isnull().sum())

   
    def statistics(self):

        print("\n========== DESCRIPTIVE STATISTICS ==========")
        print(self.df.describe())

    def plot_distribution(self):

        numeric_cols = self.df.select_dtypes(include=np.number).columns

        if len(numeric_cols) == 0:
            print("No numerical columns found.")
            return

        if "age" in numeric_cols:
            column = "age"
        else:
            column = numeric_cols[0]

        plt.figure(figsize=(8,6))
        plt.hist(
            self.df[column],
            bins=20,
            color="skyblue",
            edgecolor="black"
        )

        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.show()


def python_collections(df):

    print("\n========== LIST ==========")
    column_list = list(df.columns)
    print(column_list)

    print("\n========== TUPLE ==========")
    shape_tuple = df.shape
    print(shape_tuple)

    print("\n========== DICTIONARY ==========")
    datatype_dict = dict(df.dtypes)

    for key, value in datatype_dict.items():
        print(key, ":", value)


def numpy_operations(df):

    numeric_df = df.select_dtypes(include=np.number)

    if numeric_df.empty:
        print("No numerical columns found.")
        return

    array = numeric_df.to_numpy()

    print("\n========== NUMPY ARRAY ==========")
    print(array[:5])

    print("\nShape:", array.shape)

    print("\nMean:")
    print(np.mean(array, axis=0))

    print("\nMaximum:")
    print(np.max(array, axis=0))

    print("\nMinimum:")
    print(np.min(array, axis=0))


def broadcasting_example(df):

    numeric_df = df.select_dtypes(include=np.number)

    if numeric_df.empty:
        return

    array = numeric_df.to_numpy()

    mean = np.mean(array, axis=0)

    normalized = array - mean

    print("\n========== BROADCASTING ==========")
    print(normalized[:5])


def main():

    try:
        fifa_df = load_data(filename)

    except FileNotFoundError:
        print("CSV File Not Found!")
        print(filename)
        return

    analysis = FIFAAnalysis(fifa_df)

    analysis.dataset_info()

    analysis.clean_data()

    analysis.statistics()

    python_collections(fifa_df)

    numpy_operations(fifa_df)

    broadcasting_example(fifa_df)

    analysis.plot_distribution()


if __name__ == "__main__":
    main()