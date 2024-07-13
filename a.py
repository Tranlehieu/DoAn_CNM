# Cài đặt các thư viện cần thiết
import dash
from dash import dcc
from dash import  html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))

import numpy as np

# Khởi tạo ứng dụng Dash
app = dash.Dash()
server = app.server

# Đọc dữ liệu, sắp xếp theo ngày, lấy cột ngày và giá đóng cửa
df_nse = pd.read_csv("NSE-TATA.csv")

df_nse["Date"]=pd.to_datetime(df_nse.Date,format="%Y-%m-%d")
df_nse.index=df_nse['Date'].values

data=df_nse.sort_index(ascending=True,axis=0)
new_data=pd.DataFrame(index=range(0,len(df_nse)),columns=['Date','Close'])

for i in range(0,len(data)):
    new_data.loc[i, "Date"]=data['Date'].iloc[i]
    new_data.loc[i, "Close"]=data["Close"].iloc[i]

new_data.index=new_data['Date'].values
new_data.drop("Date",axis=1,inplace=True)
new_data.head()

# Chuẩn hóa dữ liệu
dataset=new_data.values

train=dataset[0:987,:]
valid=dataset[987:,:]

scaler=MinMaxScaler(feature_range=(0,1))
scaled_data=scaler.fit_transform(dataset)

x_train,y_train=[],[]

for i in range(60,len(train)):
    x_train.append(scaled_data[i-60:i,0])
    y_train.append(scaled_data[i,0])

x_train,y_train=np.array(x_train),np.array(y_train)

x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))

# Lấy mẫu từ dữ liệu để đưa ra dự đoán giá cổ phiếu bằng mô hình LSTM:

model=load_model("saved_lstm_model.keras")

inputs=new_data[len(new_data)-len(valid)-60:].values
inputs=inputs.reshape(-1,1)
inputs=scaler.transform(inputs)

X_test=[]
for i in range(60,inputs.shape[0]):
    X_test.append(inputs[i-60:i,0])
X_test=np.array(X_test)

X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
closing_price=model.predict(X_test)
closing_price=scaler.inverse_transform(closing_price)

train=new_data[:987]
valid=new_data[987:]

valid.loc[:, 'Predictions_LSTM'] = closing_price

print(valid)

# Lấy mẫu từ dữ liệu để đưa ra dự đoán giá cổ phiếu bằng mô hình RNN:

model=load_model("saved_rnn_model.keras")

inputs=new_data[len(new_data)-len(valid)-60:].values
inputs=inputs.reshape(-1,1)
inputs=scaler.transform(inputs)

X_test=[]
for i in range(60,inputs.shape[0]):
    X_test.append(inputs[i-60:i,0])
X_test=np.array(X_test)

X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))

closing_price=model.predict(X_test)
closing_price=scaler.inverse_transform(closing_price)

valid.loc[:, 'Predictions_RNN'] = closing_price

print(valid)

