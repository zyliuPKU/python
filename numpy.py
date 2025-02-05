#1.shape
X=np.array([1,2,3],[4,5,6])
X.shape #(2,3)

#2.arrange
X=np.arrange(1,13) #np.array(1,2,...,12)

#3.reshape
X=np.arrange(1,13)
np.reshape(X,(3,4)) #[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
np.reshape(X,(-1,1)) #-1是自适应行数
