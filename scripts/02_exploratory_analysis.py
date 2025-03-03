import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def exploratory_analysis(file_path):
    df = pd.read_csv(file_path)

    # Summary statistics
    print(df.describe())

    # Correlation matrix
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Feature Correlation Matrix")
    plt.savefig("outputs/correlation_matrix.png")

    # Histograms
    df.hist(figsize=(12, 8))
    plt.savefig("outputs/histograms.png")

if __name__ == "__main__":
    exploratory_analysis("outputs/cleaned_data.csv")
