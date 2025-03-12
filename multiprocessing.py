import multiprocessing as mlp

def func(dates):
  return
  
if __name__ == '__main__':
    #1.Pool
    args=[1,2,3]
    n=mlp.cpu_count()
    with mlp.Pool(n) as p:
        p.map(func, args)
      
    #2.Process
    p=mlp.Process(target=func,args=(1,))
    p.start()
    p.join()
  
    #3.Queue
    q=mlp.Queue()
    q.put(1)
    q.get()
  
