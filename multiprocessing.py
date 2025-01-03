import multiprocessing as mlp

def func(dates):
  return
  
if __name__ == '__main__':
    batch_size = 20
    dates=range(1, 1000)
    dates_batch=[dates[i:i+batch_size] for i in range(0, len(dates), batch_size)]
    n=mlp.cpu_count()
    with mlp.Pool(n) as p:
        p.map(func, dates_batch)
