# 🔬 Magnesium Alloy Mechanical Property Prediction

An intelligent Machine Learning-based application for predicting the mechanical properties of Mg-Zn-Zr-Y magnesium alloys using Yttrium (Y) concentration.

## 🚀 Live Application

**[Launch Magnesium Alloy ML Predictor](https://magnesium-alloy-property-prediction-application-by-devendra.streamlit.app/)**

## 📌 Project Overview

This project uses Machine Learning models to predict the mechanical properties of magnesium alloys based on their chemical composition.

The application allows users to adjust Yttrium concentration while keeping Zinc (Zn) and Zirconium (Zr) concentrations fixed, and generates predictions for multiple mechanical properties through an interactive Streamlit interface.

## ✨ Key Features

- **Mechanical Property Prediction:** Predicts five important mechanical properties.
- **Interactive Composition Input:** Adjust Yttrium concentration using an interactive slider.
- **Multiple ML Models:** Uses trained regression models for different mechanical properties.
- **Performance Analysis:** Provides an overall performance analysis of predicted properties.
- **Interactive Dashboard:** Clean and user-friendly Streamlit interface.
- **Visual Analytics:** Includes graphical comparisons and performance visualizations.

## ⚙️ Predicted Mechanical Properties

| Property | Unit |
|---|---|
| Tensile Strength | MPa |
| Fatigue Strength | MPa |
| Compressive Strength | MPa |
| Creep Rate | s⁻¹ |
| Hardness | HV |

## 🧪 Alloy Composition

- **Base Material:** Magnesium (Mg)
- **Fixed Elements:** Zinc (Zn) and Zirconium (Zr)
- **Variable Element:** Yttrium (Y)

The application explores how variations in Yttrium concentration influence the predicted mechanical properties.

## 🛠️ Technology Stack

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Web Framework:** Streamlit
- **Model Serialization:** Joblib

## 📂 Project Structure

```text
magnesium-alloy-property-prediction/
│
├── app.py
├── main.py
├── eda.py
├── preprocessing.py
├── model_training.py
├── model_analysis.py
├── prediction_analysis.py
├── performance_score.py
│
├── best_models.pkl
├── best_model_summary.csv
├── model_comparison.csv
├── overall_performance_results.csv
│
├── Mg_Zn_Zr_Y_synthetic_demo_1000.xlsx
│
├── requirements.txt
│
└── *.png
```

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DevendraKumar577/magnesium-alloy-property-prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd magnesium-alloy-property-prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

## 📊 Dataset

The repository includes a 1,000-row synthetic demonstration dataset for Mg-Zn-Zr-Y alloy analysis.

**Dataset:** `Mg_Zn_Zr_Y_synthetic_demo_1000.xlsx`

## 🎯 Project Objective

The primary objective is to demonstrate how Machine Learning can support mechanical property prediction and composition-based analysis of magnesium alloys.

## 👨‍💻 Author

**Devendra Kumar**

B.Tech – Materials & Metallurgical Engineering

Maulana Azad National Institute of Technology (MANIT), Bhopal
