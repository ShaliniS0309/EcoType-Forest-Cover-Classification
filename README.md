# 🌿 EcoType – Forest Cover Type Classification

## 📌 Overview
EcoType is a machine learning project that predicts the **forest cover type** of a geographical area using cartographic and environmental features such as elevation, slope, hillshade, and distances to hydrology, roads, and fire points.

---

## 🎯 Objective
To build and deploy a machine learning model that classifies forest cover types and provides real-time predictions using a Streamlit web application.

---

## 🌍 Domain
Environmental Data Science & Geospatial Predictive Modeling

---

## 📊 Dataset
- Forest Cover Type Dataset  
- Records: 145,891  
- Features: 13  
- Target Variable: `Cover_Type` (7 classes)

### Target Classes
1. Spruce / Fir  
2. Lodgepole Pine  
3. Ponderosa Pine  
4. Cottonwood / Willow  
5. Aspen  
6. Douglas-fir  
7. Krummholz  

---

## 🛠 Technologies
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Joblib  
- Streamlit  

---

## 🤖 Models Used
- Logistic Regression  
- KNN  
- Decision Tree  
- Random Forest  
- XGBoost  

**Best Model:** Random Forest / XGBoost

---

## 🌐 Streamlit App
Users can input environmental values and predict the forest cover type instantly.

**Sample Output:**
Predicted Forest Cover Type: Spruce / Fir


---

## 📁 Project Structure
Forest_Cover_Classification/
├── classification.py
├── forest_model.pkl
├── encoder.pkl
├── README.md
└── requirements.txt


---
## ▶️ How to Run
```bash
pip install -r requirements.txt
streamlit run classification.py
```
---
## ✅ Conclusion
This project demonstrates the effective use of machine learning techniques to classify forest cover types based on cartographic and environmental features. The trained model is deployed using a Streamlit web application, providing a simple and interactive interface for real-time forest cover prediction.





