import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[np.nan,np.nan,np.nan],'C':[1,2,3]}

df = pd.DataFrame(d)

df['A'].fillna(value=df['A'].mean())