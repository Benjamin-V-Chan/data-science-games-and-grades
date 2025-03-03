import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def preprocess_data(file_path):
    df = pd.read_csv(file_path)

    # Normalize numerical columns (except target)
    scaler = StandardScaler()
    num_cols = ["Playing Years", "Playing Often", "Playing Hours", "Playing Games", "Parent Revenue", "Father Education", "Mother Education"]
    df[num_cols] = scaler.fit_transform(df[num_cols])

    # Save processed dataset
    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/processed_data.csv", index=False)

if __name__ == "__main__":
    preprocess_data("outputs/cleaned_data.csv")
