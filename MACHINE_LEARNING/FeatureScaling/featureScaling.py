from sklearn.preprocessing import StandardScaler,MinMaxScaler

scaler=StandardScaler()
x_scaled=scaler.fit_transform()

scaler=MinMaxScaler()
x_scaled=scaler.fit_transform()