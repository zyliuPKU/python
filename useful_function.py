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


