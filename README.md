# data-science-games-and-grades

# Project Overview
This project analyzes the relationship between gaming habits and student academic performance. Using regression models, it predicts student grades based on gaming time, parental education, and other factors. The dataset used is "Games and Success in Students."

# Folder Structure
```
project-root/
├── data/            # Contains the dataset
├── scripts/         # Python scripts for data processing and analysis
├──── 01_load_data.py: Load, explore, and clean the dataset.
├──── 02_exploratory_analysis.py: Perform summary statistics and visualize data distributions.
├──── 03_feature_engineering.py: Process categorical variables, create new features if needed.
├──── 04_model_training.py: Train regression models to predict Grade.
├──── 05_evaluation.py: Evaluate model performance using RMSE, R², and other metrics.
├──── 06_visualizations.py: Create visualizations for insights.
├──── 07_predictions.py: Use the trained model to predict grades for new inputs.
├── outputs/         # Stores cleaned data, models, and visualizations
├── requirements.txt # Required dependencies
└── README.md        # Project documentation
```

# Usage
### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```sh
pip install -r requirements.txt
```

### 2. Load and Clean Data:
```sh
python scripts/01_load_data.py
```

### 3. Perform Exploratory Data Analysis:
```sh
python scripts/02_exploratory_analysis.py
```

### 4. Feature Engineering:
```sh
python scripts/03_feature_engineering.py
```

### 5. Train Models:
```sh
python scripts/04_model_training.py
```

### 6. Evaluate Models:
```sh
python scripts/05_evaluation.py
```

### 7. Generate Visualizations:
```sh
python scripts/06_visualizations.py
```

### 8. Make Predictions:
```sh
python scripts/07_predictions.py
```

# Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- joblib

# Acknowledgments
**Dataset Name:** Games and Success in Students  
**Dataset Author:** Ali Kemal Cimşit  
**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/deadier/play-games-and-success-in-students)