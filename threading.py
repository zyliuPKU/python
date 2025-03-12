import threading

def f(x):
  return x*x

#1.Thread
t=threading.Thread(target=f,args=(1,))
t.start()
t.join()

#2.Lock
lock=threading.Lock()
res=[]
def f():
  for i in range(10):
    with lock:
      res.append(1)
      res[-1]+=1
threads = [threading.Thread(target=worker) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()


    
