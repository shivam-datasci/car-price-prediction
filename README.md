# 🚗 Car Price Prediction Using Machine Learning
[![Open In NBViewer](https://img.shields.io/badge/Open%20in-NBViewer-orange?logo=jupyter)](https://nbviewer.org/github/shivam-datasci/car-price-prediction/blob/main/car_price_prediction.ipynb)

## 📌 Project Overview

This project aims to **predict the price of used cars** based on various features such as brand, fuel type, mileage, transmission, and more. We apply and compare three machine learning regression algorithms to evaluate their performance:

- ✅ Linear Regression
- ✅ Decision Tree Regressor
- ✅ Random Forest Regressor

Our goal is to find the most accurate model for predicting car prices and understand how each model performs on real-world data.

---

## 🧠 Algorithms Used

| Algorithm              | Description                                      |
|------------------------|--------------------------------------------------|
| Linear Regression      | A simple model that assumes a linear relationship between features and target |
| Decision Tree Regressor| A model that splits data into branches to make predictions |
| Random Forest Regressor| An ensemble model that uses multiple decision trees to improve prediction accuracy |

---

## 🧪 Evaluation Metrics

To evaluate model performance, we used the following metrics:

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score (Coefficient of Determination)**

| Model                  | MAE       | MSE       | RMSE      | R² Score  |
|------------------------|-----------|-----------|-----------|-----------|
| Linear Regression      | 0.2622    | 0.1328    | 0.3645    | 0.8931    |
| Decision Tree Regressor| 0.2266    | 0.1151    | 0.3393    | 0.9073    |
| Random Forest Regressor| 0.1538    | 0.0501    | 0.2238    | 0.9596    |

📌 **Conclusion:**  
The **Random Forest Regressor** outperformed the other two models with the highest R² Score (≈ 96%) and the lowest error values. It is the most suitable model for our dataset.

---

## 🗂️ Dataset Info

- Source: [You may mention the original dataset source or upload it in the repo]
- Format: CSV
- Size: Small/Medium
- Features include: Car name, fuel type, seller type, mileage, engine size, transmission, etc.

---

## 🧰 Technologies Used

- **Python**
- **Jupyter Notebook**
- **Pandas, NumPy**
- **Matplotlib, Seaborn** (for visualization)
- **Scikit-learn** (for ML algorithms and preprocessing)

---

## 📊 Visualizations

We used visual plots such as:

- Distribution of car prices
- Bar plots to compare model performance
- Scatter plots for actual vs predicted values

---

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/car-price-prediction.git
