from sklearn import datasets #自带数据集
iris=datasets.load_iris() #一个字典
X=iris.data #n*k,n是样本数,k是特征数
y=iris.target

from sklearn.model_selection import train_test_split #训练集和测试集划分
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

from sklearn import preprocessing
scaler=preprocessing.StandardScaler()
scaler=preprocessing.MinMaxScaler()
scaler.fit(X_train)
X_train=scaler.transform(X_train)

from sklearn.model_selection import KFold #k折交叉验证
kf=KFold(n_splits=5,shuffle=True,random_state=0) #在每个epoch打乱样本
for train_index,test_index in kf.split(X):
  X_train,X_test=X[train_index],X[test_index]
  y_train,y_test=y[train_index],y[test_index]
  
from sklearn import linear_model
reg=linear_model.LinearRegression(fit_intercept=False) #截距默认True
reg=linear_model.Lasso(alpha=0.1,fit_intercept=False)
reg=linear_model.Ridge(alpha=0.1,fit_intercept=False)

reg.fit(X_train,y_train)
reg.coef_
reg.intercept_
y_pred=reg.predict(X_test)

from sklearn import metrics
metrics.mean_squared_error(y_test,y_pred) # E(yt-yp)^2
metrics.mean_absolute_error(y_test,y_pred) # E|yt-yp|
metrics.r2_score(y_test,y_pred) #1-(yt-yp)^2/(yt-yt_bar)^2

