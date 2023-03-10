import pandas as pd
import dask.dataframe as dd
import numpy as np
from dask.multiprocessing import get
import timeit

data = pd.DataFrame()
data['col1'] = np.random.normal(size = 1500000)
data['col2'] = np.random.normal(size = 1500000)

ddata = dd.from_pandas(data, npartitions=30)
def myfunc(x,y): return y*(x**2+1)
def apply_myfunc_to_DF(df): return df.apply((lambda row: myfunc(*row)), axis=1)
def pandas_apply(): return apply_myfunc_to_DF(data)
def dask_apply(): return ddata.map_partitions(apply_myfunc_to_DF).compute()  
def vectorized(): return myfunc(data['col1'], data['col2']  )

t_pds = timeit.Timer(lambda: pandas_apply())
print(t_pds.timeit(number=1))

t_dsk = timeit.Timer(lambda: dask_apply())
print(t_dsk.timeit(number=1))

t_vec = timeit.Timer(lambda: vectorized())
print(t_vec.timeit(number=1))