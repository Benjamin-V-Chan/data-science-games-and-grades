import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_visualizations(file_path):
    df = pd.read_csv(file_path)

    # Scatter plot of Playing Hours vs. Grade
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df["Playing Hours"], y=df["Grade"])
    plt.xlabel("Playing Hours")
    plt.ylabel("Grade")
    plt.title("Playing Hours vs. Grade")
    plt.savefig("outputs/playing_hours_vs_grade.png")

if __name__ == "__main__":
    generate_visualizations("outputs/cleaned_data.csv")
