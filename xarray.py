import xarray as xr
import numpy as np

#生成dataarray
dates=['20090101','20090102']
stocks=['stocks1','stocks2']
values=['v1','v2']
data=np.random.randn(len(dates),len(stocks),len(values))
da=xr.DataArray(data,dims=['d','s','v'],coords=[dates,stocks,values])

#更改坐标刻度
#方法一
dates2=['date1','date2']
da['d']=dates2
da['d'] #获取坐标刻度
#方法二
da=da.assign_coords(d=dates2)

#更改坐标名称
da=da.rename(d='time')

#合并dataarray
da=xr.concat([da1,da2],dim='v') 

#选定坐标
#方法一
da.sel(d='20090101') #d维度就没了
da.sel(d=['20090101']) #d维度还有
#方法二
da.loc['20090101','stock1','v1']
da.loc['20090101','stock1','v1']=100 #赋值
da.loc[['20090101','20090102'],'stock1']

#获得数据
da.values

#获得坐标名
da.dims

#获得坐标和刻度
da.coords

#整体方法
da.mean(dim='d')
da.sum(dim='d')
da.prod(dim='d')
da.median(dim='d')
da.min(dim='d')
da.max(dim='d')
da.argmin(dim='d')
da.argmax(dim='d')
da.std(dim='d')
da.var(dim='d')
da.rank(dim='d')
da.cumsum(dim='d')
da.cumprod(dim='d')
da.diff(dim='d')
da.shift(d=1)#昨天的值放到今天的坐标下
da.fillna(0)
da.dropna(dim='d')
da.quantile(dim='d',q=0.1)

#滚动方法
da.rolling(d=2,min_periods=1).mean() #滚动包含当天，min_periods是窗口中至少包含多少不是nan的，默认等于设定窗口长度
da.rolling(d=2,min_periods=1).sum()
da.rolling(d=2,min_periods=1).prod()
da.rolling(d=2,min_periods=1).median()
da.rolling(d=2,min_periods=1).min()
da.rolling(d=2,min_periods=1).max()
da.rolling(d=2,min_periods=1).argmin()
da.rolling(d=2,min_periods=1).argmax()
da.rolling(d=2,min_periods=1).std()
da.rolling(d=2,min_periods=1).var()
da.rolling(d=2,min_periods=1).count() #计数有多少不是nan的

da.rolling(d=2,min_periods=1).construct('w').quantile(dim='w',q=0.1)
da.rolling(d=2,min_periods=1).construct('w').rank(dim='w')
wgt=[1,2]
(da.rolling(d=2,min_periods=1).construct('w')*wgt).sum(dim='w')#内积

#自定义方法
xr.apply_ufunc(norm.ppf,da)

#生成nc文件
da.to_netcdf('data.nc')
#读取文件
da=xr.open_dataarray('data.nc')
