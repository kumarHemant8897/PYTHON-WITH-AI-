from sklearn.metrics import  mean_absolute_error,mean_squared_error
import numpy as np

#reak score
real_score=[90,60,80,100]

#predicted val
pred_scor=[85,70,70,90]

mae=mean_absolute_error(real_score,pred_scor)
print("mean squre error: ")
print(mae)

mse=mean_squared_error(real_score,pred_scor)
print("mean squred error :  ")
print(mse)

rmse=np.sqrt(mse)
print("RMSE ROOT MEAN SQURE:  " )
print(rmse)