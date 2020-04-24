import numpy as np
import pandas as pd
from numpy.random import randn

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
heir_index = list(zip(outside,inside))
heir_index = pd.MultiIndex.from_tuples(heir_index)

df = pd.DataFrame(randn(6,2),heir_index,['A','B'])

df.loc['G1']

df.index.names = ['Groups', 'Num']

df.xs(1, level='Num')