# plp_advance-assignments
# 🤖 Diabetes Prediction Using Machine Learning

### 🎯 SDG Goal: Good Health and Well-being (SDG 3)

This project demonstrates how machine learning can support Sustainable Development Goal 3 by predicting the likelihood of diabetes in individuals based on health-related data.

---

## 📌 Project Overview
- **ML Task**: Binary classification
- **Model Used**: Logistic Regression
- **Dataset**: PIMA Indian Diabetes Dataset
- **Language**: Python 3
- **Libraries**: pandas, sklearn, seaborn, matplotlib

---

## 📊 Dataset Description
- **Pregnancies**
- **Glucose**
- **Blood Pressure**
- **Skin Thickness**
- **Insulin**
- **BMI**
- **Diabetes Pedigree Function**
- **Age**
- **Outcome** (0 = Non-diabetic, 1 = Diabetic)

📁 Source: [Kaggle Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---

## ⚙️ How It Works
1. Load and explore the dataset
2. Visualize feature correlations
3. Preprocess and normalize the data
4. Train a logistic regression classifier
5. Evaluate the model performance using accuracy and F1-score
6. Visualize confusion matrix

---

## 🔍 Results
- Model trained with 80/20 train-test split
- Achieved good accuracy and precision on unseen data

Example classification report output:
```
              precision    recall  f1-score   support

           0       0.81      0.89      0.85        99
           1       0.74      0.61      0.67        55

    accuracy                           0.79       154
   macro avg       0.77      0.75      0.76       154
weighted avg       0.78      0.79      0.78       154
```

---

## 📷 Screenshots
> Add screenshots of:
- Data visualizations (heatmaps, scatter plots)
- Model output (confusion matrix, classification report)

---

## 🔐 Ethical Considerations
- Dataset only includes PIMA women — lacks gender/racial diversity
- Must be cautious when deploying in broader populations
- Highlights the need for inclusive data collection in healthcare

---

## 📁 File Structure
```
├── diabetes_prediction.py
├── README.md
└── screenshots/
```

---

## 🙌 Contribution
Built by [Your Name] as part of the PLP Academy Week 2 Assignment.

---

## 🌍 Why This Matters
Using AI to detect diabetes early can:
- Help reduce healthcare costs
- Encourage early treatment and lifestyle changes
- Support global efforts toward achieving health equity

> “AI can be the bridge between innovation and sustainability.” — UN Tech Envoy
