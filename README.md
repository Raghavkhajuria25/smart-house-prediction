# 🏠 Smart House Price Prediction

> 🤖 A Machine Learning based web application for predicting house prices using Python, Streamlit and MySQL.

## 🚀 Overview

**Smart House Price Prediction** is an interactive Machine Learning project that predicts the estimated price of a house based on different property features.

The application provides a simple interface where users can enter property details and instantly get an estimated house price.

## ✨ Features

- 🏠 House Price Prediction
- 🤖 Linear Regression Machine Learning Model
- 📊 Price Distribution Analysis
- 📈 Area vs Price Visualization
- 💾 MySQL Database Integration
- 📋 Prediction History
- 📊 Dataset Statistics
- 🎨 Interactive Streamlit Dashboard

## 🧠 Machine Learning

The project uses **Linear Regression** for house price prediction.

### Input Features

- 📐 Area
- 🛏️ Bedrooms
- 🛁 Bathrooms
- 🏢 Floors
- 🕐 Age of House
- 📍 Location Score

### Prediction

The trained model uses these features to estimate the house price.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core Programming |
| 🤖 Scikit-learn | Machine Learning |
| 🐼 Pandas | Data Processing |
| 🔢 NumPy | Numerical Operations |
| 🎨 Streamlit | Web Application |
| 🗄️ MySQL | Database |
| 📊 Matplotlib | Data Visualization |

## 📊 Dashboard

The application includes:

**🏡 Prediction**
  
Enter property details and get an estimated house price.

**📋 Prediction History**
  
Previous predictions are stored and displayed using MySQL.

**📈 Data Analytics**
  
Visualizations help understand the relationship between house area and price.

## 📁 Project Structure

```text
smart-house-prediction/
│
├── app.py
├── database.py
├── train_model.py
├── house_price.csv
├── model.pkl
└── README.md
