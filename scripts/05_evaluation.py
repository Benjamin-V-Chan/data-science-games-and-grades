import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model_path, test_data_path):
    df = pd.read_csv(test_data_path)
    X = df.drop(columns=["Grade"])
    y = df["Grade"]

    model = joblib.load(model_path)
    y_pred = model.predict(X)

    # Compute metrics
    rmse = mean_squared_error(y, y_pred, squared=False)
    r2 = r2_score(y, y_pred)

    print(f"Model: {model_path}, RMSE: {rmse:.2f}, R²: {r2:.2f}")

if __name__ == "__main__":
    for model_name in ["linear_regression", "random_forest"]:
        evaluate_model(f"outputs/{model_name}.pkl", "outputs/processed_data.csv")
