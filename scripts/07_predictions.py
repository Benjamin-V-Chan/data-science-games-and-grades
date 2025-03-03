import pandas as pd
import joblib

def make_prediction(model_path, input_data):
    model = joblib.load(model_path)
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    return prediction

if __name__ == "__main__":
    new_input = {
        "Sex": 0,
        "School Code": 1,
        "Playing Years": 2,
        "Playing Often": 3,
        "Playing Hours": 4,
        "Playing Games": 2,
        "Parent Revenue": 3,
        "Father Education": 4,
        "Mother Education": 5
    }
    
    predicted_grade = make_prediction("outputs/random_forest.pkl", new_input)
    print(f"Predicted Grade: {predicted_grade:.2f}")
