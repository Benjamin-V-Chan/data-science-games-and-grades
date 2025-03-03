import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_models(file_path):
    df = pd.read_csv(file_path)
    
    X = df.drop(columns=["Grade"])
    y = df["Grade"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train models
    models = {
        "linear_regression": LinearRegression(),
        "random_forest": RandomForestRegressor(n_estimators=100, random_state=42)
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        joblib.dump(model, f"outputs/{name}.pkl")

if __name__ == "__main__":
    train_models("outputs/processed_data.csv")
