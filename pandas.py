import pandas as pd

#构建dataframe
#方法一
df=pd.DataFrame({'a':[1,2,3],'b':[4,5,6]},index=['x','y','z'])
#方法二
data=[[1,2],[3,4],[5,6]]
df=pd.DataFrame(data,columns=['a','b'],index=['x','y','z'])

#获取,更改列名
df.columns
df.columns=['a1','b1']
df.rename(columns={'a':'a1'},inplace=True)
#获取,更改行名
df.index
df.index=['x1','y1','z1']
df.rename(index={'x':'x1'},inplace=True)

#查询
df['a'] #查询列名
df.loc['x','a'] #查询先行名后列名
df.loc['x']
df.iloc[0] #查询第i行

#获取数据
df.values

#函数
df.sum(axis=1) #把一行加起来
df.sum(axis=0) #把一列加起来,默认是列
df.mean()
df.prod()
df.min()
df.max()
df.median()
df.std()
df.var()
df.shift(1,axis=0)#每一行移动一列
df.diff()
df.pct_change()
df.cov() #计算每一列之间的协方差，不能指定axis
df.corr() #计算每一列之间的相关系数，不能指定axis
df.rank()
df.cumsum()
df.cumprod()
df.cummax()
df.cummin()
df.apply(np.sqrt)


df.rolling(2,min_periods=1).sum()
df.rolling(2,min_periods=1).mean()
df.rolling(2,min_periods=1).std()
df.rolling(2,min_periods=1).var()
df.rolling(2,min_periods=1).median()
df.rolling(2,min_periods=1).max()
df.rolling(2,min_periods=1).min()
df.rolling(2,min_periods=1).quantile(0.1)
df.rolling(2,min_periods=1).corr()
df.rolling(2,min_periods=1).cov()
df.rolling(2,min_periods=1).rank()

df.rolling(2,min_periods=1).apply(lambda x:x.max()-x.min())


#生成文件
df.to_csv('data.csv')
#读取文件
pd.read('data.csv',index_col=0)
