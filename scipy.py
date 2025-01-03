#scipy.stats提供了很多常见的分布
from scipy.stats import norm,t,chi2

norm.ppf(0.95) #百分位对应的标准正态值
norm.pdf(1.96) #概率密度
norm.cdf(1.96) #累计概率

#还有很多常用量
from scipy.stats import skew,kurtosis
skew([1,2,3,4,5])