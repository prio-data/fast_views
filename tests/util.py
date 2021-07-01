import numpy as np
import pandas as pd

def randint_seed(a: int, b:int, seed: int):
    """
    Returns a random number between a and b that is always the same for each seed.
    """
    h = str(hash(str(seed)))
    seed_n = h[-4:].zfill(4)
    seed_factor = int(seed_n) / 9999
    return a + int((b-a)*seed_factor)

def time_unit_column_df(name:str, max_units: int = 60000, min_time = 1, max_time: int = 100):
    indices = []
    for i in range(min_time, max_time):
        for j in range(randint_seed(1,max_units,i)):
            indices.append((i,j))
    return pd.DataFrame(
            np.ones((len(indices),1)),
            index=pd.MultiIndex.from_tuples(indices),
            columns=[name])
