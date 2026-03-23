# 📦 Food Delivery Time Prediction

## 📌 Project Overview

This project aims to predict food delivery time using machine learning based on various operational and environmental factors such as distance, traffic level, weather conditions, preparation time, and courier experience.

The goal is to build an accurate prediction model that can help improve delivery efficiency and customer satisfaction.

---

## 🎯 Objectives

* Predict delivery time using regression models
* Identify key factors affecting delivery performance
* Compare multiple machine learning models
* Deploy the best model into a simple web application

---

## 📊 Dataset Features

* Distance (km)
* Weather condition
* Traffic level
* Time of day
* Vehicle type
* Preparation time (minutes)
* Courier experience (years)

Target:

* Delivery Time (minutes)

---

## 🤖 Models Used

* Linear Regression ✅ (Best Model)
* Ridge Regression
* Lasso Regression
* Random Forest
* XGBoost

---

## 🏆 Model Performance

| Model                 | RMSE     |
| --------------------- | -------- |
| Linear Regression     | **8.82** |
| Ridge Regression      | 8.84     |
| Lasso Regression      | 8.84     |
| XGBoost (Tuned)       | 9.55     |
| Random Forest (Tuned) | 10.26    |

📌 Linear Regression achieved the best performance, indicating that the dataset has a predominantly linear relationship between features and target.

---

## 🧠 Key Insights

* Distance is the most influential factor in delivery time
* Traffic significantly increases delivery delays
* Preparation time contributes moderately
* Courier experience has minimal impact

---

## 🚀 Deployment

The best model (Linear Regression) is deployed using **Streamlit** to create an interactive web application where users can input delivery conditions and receive predicted delivery time.

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Conclusion

This project demonstrates that simpler models can outperform complex models when the underlying data relationships are linear. Model selection should always be driven by data characteristics rather than model complexity.
