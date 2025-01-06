import statsmodels.api as sm
import numpy as np

#线性回归
X=np.arange(100).reshape(-1,1)
y=X+np.random.normal(0,10,100).reshape(-1,1)

# X=sm.add_constant(X)
model=sm.OLS(y,X).fit(cov_type='HC0')#异方差稳健标准误

model.summary()
model.params #系数,第0个是截距
model.predict(X)

#时间序列
arr=[0]
for i in range(100):
  arr.append(arr[-1]*0.8+np.random.normal(0,1))
model=sm.tsa.ARIMA(arr,order=(1,0,0)).fit() #(p,d,q),p是自回归阶数,d是差分阶数,q是移动平均阶数

model.summary()
model.params
model.predict(start=0,end=len(arr)-1) #模型预测期望
