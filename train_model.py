import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv(r"C:\project\smart house prediction\house_price.csv")


X = df[[
    "Area",
    "Bedrooms",
    "Bathrooms",
    "Floors",
    "Age",
    "LocationScore"
]]

y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

score = r2_score(y_test, y_pred)

print("\nModel Accuracy:", round(score, 2))

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Saved Successfully")