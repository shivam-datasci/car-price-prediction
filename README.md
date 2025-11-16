# 🚗 Car Price Prediction Web App

A Machine Learning project that predicts the selling price of a car based on its specifications such as engine size, horsepower, mileage, and more.  
The final model is deployed as an interactive **Streamlit Web Application**.  

---

## 📌 Project Objective

To estimate the accurate price of a car using different regression algorithms and compare their performance.  
The best performing model is selected for deployment.

---

## 🧠 Machine Learning Models Used

| Model | R² Score | RMSE | Remarks |
|-------|---------|------|---------|
| Linear Regression | ~0.89 | High | Struggles with non-linearity |
| Decision Tree Regressor | ~0.90 | Moderate | Overfits data |
| **Random Forest Regressor (Tuned)** | **~0.96** | ✔ Best | Best model selected for deployment |

---

## ⚙️ Hyperparameter Tuning

The Random Forest model was tuned using **RandomizedSearchCV** to improve performance.

Final selected parameters:
```python
{'n_estimators': 200, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_depth': None}
