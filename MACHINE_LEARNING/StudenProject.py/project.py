import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

data = {
    "hours": [2, 3, 4, 5, 6],
    "score": [30, 40, 60, 80, 90]
}

df = pd.DataFrame(data)
print(df)

# ✅ USE df, not data
X = df[["hours"]]   # 2D
y = df["score"]     # 1D

model = LinearRegression()
model.fit(X, y)

predicted_score = model.predict(X)

mse = mean_squared_error(y, predicted_score)
mae = mean_absolute_error(y, predicted_score)
rmse = np.sqrt(mse)

print("MEAN SQUARED ERROR:", mse)
print("MEAN ABSOLUTE ERROR:", mae)
print("ROOT MEAN SQUARED ERROR:", rmse)

new_hours = float(input("Enter hours studied: "))
new_pred = model.predict([[new_hours]])

print(f"Predicted score if you study {new_hours} hours is: {new_pred[0]:.2f}")
