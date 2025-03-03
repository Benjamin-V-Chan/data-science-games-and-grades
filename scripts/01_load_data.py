import pandas as pd
import os

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    
    # Convert Grade to numeric
    df["Grade"] = pd.to_numeric(df["Grade"], errors="coerce")
    
    # Ensure no missing values
    df.dropna(inplace=True)

    # Save cleaned dataset
    output_path = "outputs/cleaned_data.csv"
    os.makedirs("outputs", exist_ok=True)
    df.to_csv(output_path, index=False)
    
    return df

if __name__ == "__main__":
    dataset_path = "data/gameandgrade.csv"
    df = load_and_clean_data(dataset_path)
