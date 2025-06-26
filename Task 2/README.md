# 🧠 Diabetes Prediction using Machine Learning

This project uses a machine learning classification model to predict whether a person has diabetes, based on various medical attributes such as glucose level, BMI, age, etc.

## 📁 Dataset

The dataset used is the [PIMA Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) from the UCI Machine Learning Repository.

- Number of Instances: 768
- Number of Attributes: 8 (plus target label)

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib & Seaborn

## 📊 Features

| Feature | Description |
|---------|-------------|
| Pregnancies | Number of times pregnant |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure (mm Hg) |
| SkinThickness | Triceps skinfold thickness (mm) |
| Insulin | 2-Hour serum insulin (mu U/ml) |
| BMI | Body mass index (weight in kg/(height in m)^2) |
| DiabetesPedigreeFunction | Diabetes pedigree function |
| Age | Age in years |
| Outcome | Class variable (0 = No Diabetes, 1 = Diabetes) |

## 🔍 Model Used

We use **Logistic Regression**, a simple yet effective classification algorithm for binary classification problems.

### Steps Followed:

1. **Data Loading** – Load and inspect the dataset.
2. **Exploratory Data Analysis (EDA)** – Visualize and understand the data.
3. **Preprocessing** – Normalize features using `StandardScaler`.
4. **Train/Test Split** – Split data into training and testing sets (80/20).
5. **Model Training** – Train a Logistic Regression model.
6. **Evaluation** – Evaluate the model using accuracy, confusion matrix, and classification report.

## 📈 Results

| Metric | Value |
|--------|-------|
| Accuracy | ~77% |
| Precision (Class 1) | 70% |
| Recall (Class 1) | 58% |
| F1-score (Class 1) | 63% |

## 📌 Future Improvements

- Try other models like Random Forest, SVM, or XGBoost.
- Use cross-validation for better evaluation.
- Handle missing or zero values more carefully.
- Feature selection/engineering to improve accuracy.

## 📂 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/diabetes-prediction.git
   cd diabetes-prediction
