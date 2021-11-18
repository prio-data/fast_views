
import pdb
import random

from operator import add
from functools import reduce
import unittest
from typing import List, Tuple
import numpy as np
import pandas as pd
from fast_views import inner_join

def df_from_indices(indices: List[Tuple[int,int]])-> pd.DataFrame:
    return pd.DataFrame(np.zeros(len(indices)), index = pd.MultiIndex.from_tuples(indices))

unique_index_values = lambda lvl, dataframes: set(reduce(add, [list(df.index.get_level_values(lvl)) for df in dataframes]))

class TestRobustFastJoin(unittest.TestCase):

    #def test_unit_mismatch(self):
    def unit_mismatch(self):
        def random_unit_indices(times, max_units):
            n_units = max_units - (np.sqrt((1 * np.random.randn(times))**2)).astype(int)

            indices = []
            for t,u in zip(range(1, times+1), n_units):
                indices += [(t,i) for i in range(u)]
            return indices

        dataframes = [df_from_indices(random_unit_indices(100, 50)) for _ in range(5)]
        units, times = (unique_index_values(i, dataframes) for i in range(1,3))

        joined = inner_join(dataframes)

        for lvl,indices in zip((1,2), (units,times)):
            self.assertEqual(unique_index_values(lvl, [joined]), indices)

    def test_time_mismatch(self):
        def random_time_indices(max_times, units, noise = .4):
            n_times = max_times - int((max_times * noise) * random.random())
            padding = int(0 + ((max_times * noise) * random.random()))
            return [(t + padding,u) for t in range(n_times) for u in range(units)]
        dataframes = [df_from_indices(random_time_indices(10,3)) for _ in range(5)]
        pdb.set_trace()

    def test_same_colnames(self):
        pass

    def test_missing_index(self):
        pass

