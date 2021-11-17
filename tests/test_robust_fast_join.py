
import pdb
import unittest
from typing import List, Tuple
import numpy as np
import pandas as pd
from fast_views import inner_join

def df_from_indices(indices: List[Tuple[int,int]])-> pd.DataFrame:
    return pd.DataFrame(np.zeros(len(indices)), index = pd.MultiIndex.from_tuples(indices))

class TestRobustFastJoin(unittest.TestCase):

    def test_unit_mismatch(self):
        def random_unit_indices(times, max_units):
            n_units = max_units - (np.sqrt((1 * np.random.randn(times))**2)).astype(int)

            indices = []
            for t,u in zip(range(1, times+1), n_units):
                indices += [(t,i) for i in range(u)]
            return indices
        dataframes = [df_from_indices(random_unit_indices(100, 50)) for _ in range(5)]
        joined = inner_join(dataframes)

    def test_time_mismatch(self):
        pass

    def test_same_colnames(self):
        pass

    def test_missing_index(self):
        pass

