import streamlit as st
import pandas as pd
import numpy as np
import pickle
import mysql.connector
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Smart House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Raghav@2003",
    database="house_db"
)

cursor = conn.cursor()

st.title("🏠 Smart House Price Prediction System")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (sq ft)", min_value=500, max_value=5000, value=1500)

    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)

    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

with col2:
    floors = st.number_input("Floors", min_value=1, max_value=5, value=2)

    age = st.number_input("Age of House", min_value=0, max_value=50, value=5)

    location_score = st.slider("Location Score", 1, 10, 7)

if st.button("Predict Price"):

    data = np.array([[
        area,
        bedrooms,
        bathrooms,
        floors,
        age,
        location_score
    ]])

    prediction = model.predict(data)

    predicted_price = float(prediction[0])

    st.success(
        f"🏡 Estimated House Price = ₹ {predicted_price:,.0f}"
    )

    query = """
    INSERT INTO predictions
    (
        area,
        bedrooms,
        bathrooms,
        floors,
        age,
        location_score,
        predicted_price
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        int(area),
        int(bedrooms),
        int(bathrooms),
        int(floors),
        int(age),
        int(location_score),
        predicted_price
    )

    cursor.execute(query, values)
    conn.commit()

    st.success("✅ Prediction Saved To Database")

st.markdown("---")
st.subheader("📋 Prediction History")

history = pd.read_sql(
    "SELECT * FROM predictions ORDER BY id DESC",
    conn
)

st.dataframe(history, use_container_width=True)

st.markdown("---")
st.subheader("📊 Data Analytics")

df = pd.read_csv("house_price.csv")

col1, col2 = st.columns(2)

with col1:

    fig1, ax1 = plt.subplots()

    ax1.hist(df["Price"])

    ax1.set_title("Price Distribution")

    st.pyplot(fig1)


with col2:

    fig2, ax2 = plt.subplots()

    ax2.scatter(
        df["Area"],
        df["Price"]
    )

    ax2.set_xlabel("Area")

    ax2.set_ylabel("Price")

    ax2.set_title("Area vs Price")

    st.pyplot(fig2)

st.markdown("---")

st.subheader("📈 Dataset Statistics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Total Houses",
        len(df)
    )

with c2:
    st.metric(
        "Average Price",
        f"₹ {int(df['Price'].mean()):,}"
    )

with c3:
    st.metric(
        "Maximum Price",
        f"₹ {int(df['Price'].max()):,}"
    )