#1.zip

arr1=[1,2,3]
arr2=['a','b','c']
for x,y in zip(arr1,arr2):
  print(x,y)
# 1,'a'
# 2,'b'
# 3,'c'

#2.enumerate

arr=['a','b','c']
for idx,item in enumerate(arr):
  print(idx,item)
# 0,'a'
# 1,'b'
# 2,'c'

#3.set&frozenset

s=set() #生成空集合
s={'x'} #生成集合
s.add(x) #添加
s.pop(x) #删除
s1|s2 #并集
s1&s2 #交集
s1-s2 #差集
frozenset(s) #不可变集合

#4.eval&repr

s='[1,2]'
eval(s) #[1,2]
s="{'a':1}"
eval(s) #{'a':1}
li=[1,2]
repr(li) #'[1,2]'

#5.collections

from collections import Counter
li=[1,2,2,2,3,3,4]
dic=Counter(li) #{1:1,2:3,3:2,4:1}

#6.isinstance

isinstance(li,list) #True or False

#7.functools

#7.1 lru_cache
from functools import lru_cache
@lru_cache(1000) #缓存
def f(x):
  if x<=1 or x>=100:
    return x
  return f(x-1)+f(x+1)
  
#7.2 reduce
from functools import reduce
li=[1,2,3,4,5,6]
reduce(lambda x,y:x+y,li)

#8.recursion

import sys
sys.setrecursionlimit(3000) #最大递归深度

#9.try

try:
  x+=1
except ValueError:
  print('error')

#10.map

map(func,li)
list(map(lambda x:x**2,li))

#11.filter

filter(cond,li)
list(filter(lambda x:x<10,li))

#12.* 

li=[1,2,3,4]
a,*_=li #a=1,_=[2,3,4]
