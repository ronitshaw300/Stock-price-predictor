import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import joblib
import matplotlib.pyplot as plt

# ------------------------------
# Load model and data from app.py
# ------------------------------
try:
    model = joblib.load("stock_model.pkl")
    data = pd.read_csv("stock_data.csv")
    print("✅ Loaded model and data from app.py")
except Exception as e:
    print("❌ Could not load files. Make sure you ran app.py first.")
    print("Error:", e)
    exit()

print("Data length:", len(data))

# ------------------------------
# Safety check for small datasets
# ------------------------------
if len(data) < 5:
    print("❌ Too little data (<5 rows). Please collect more stock data before evaluating.")
    exit()

# Dynamically choose forecast_days
forecast_days = min(15, max(1, len(data) // 4))
print(f"Using forecast_days = {forecast_days}")

# ------------------------------
# Prepare data
# ------------------------------
data["Prediction"] = data["Close"].shift(-forecast_days)

# Drop missing values safely
valid_data = data.dropna(subset=["Close", "Prediction"])
if valid_data.empty:
    print("❌ No valid rows after shifting. Try using a smaller forecast_days value.")
    exit()

X = np.array(valid_data[["Close"]])
y = np.array(valid_data["Prediction"])

if len(X) == 0 or len(y) == 0:
    print("❌ Empty dataset after slicing — check your CSV or forecast_days.")
    exit()

# ------------------------------
# Predict using loaded model
# ------------------------------
try:
    predicted = model.predict(X)
except Exception as e:
    print("❌ Prediction failed. Check if your model expects scaled or multi-feature input.")
    print("Error:", e)
    exit()

# Match lengths
min_len = min(len(predicted), len(y))
predicted = predicted[:min_len]
y = y[:min_len]

# ------------------------------
# Evaluate performance
# ------------------------------
mae = mean_absolute_error(y, predicted)
rmse = np.sqrt(mean_squared_error(y, predicted))
r2 = r2_score(y, predicted)
accuracy = (1 - (mae / np.mean(y))) * 100 if np.mean(y) != 0 else 0

# ------------------------------
# Display results
# ------------------------------
print("\n📊 Model Evaluation Report:")
print(f"✅ Accuracy: {accuracy:.2f}%")
print(f"📉 Mean Absolute Error (MAE): {mae:.2f}")
print(f"📈 Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"🔹 R² Score: {r2:.4f}")

# ------------------------------
# Visualization
# ------------------------------
plt.figure(figsize=(10, 5))
plt.plot(y, label="Actual Prices", linewidth=2)
plt.plot(predicted, label="Predicted Prices", linestyle='dashed', linewidth=2)
plt.title("Model Accuracy Check (Using app.py Resources)")
plt.xlabel("Days")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True)
plt.show()
