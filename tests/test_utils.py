
import unittest
from . import util

class TestUtils(unittest.TestCase):
    def test_randint_seed_equal(self):
        a,b = (util.randint_seed(1,1000,50) for _ in range(2))
        self.assertEqual(a,b)

    def test_equal_shapes(self):
        a = util.time_unit_column_df(10, min_time = 1, max_time = 4)
        b = util.time_unit_column_df(10, min_time = 1, max_time = 4)
        self.assertEqual(a.shape, b.shape)

    def test_equal_unit_sizes(self):
        a = util.time_unit_column_df(100, min_time = 2, max_time = 4)
        b = util.time_unit_column_df(100, min_time = 1, max_time = 3)
        c = util.time_unit_column_df(100, min_time = 1, max_time = 10)
        self.assertEqual(a.loc[2,:].shape, b.loc[2,:].shape)
        self.assertEqual(b.loc[2,:].shape, c.loc[2,:].shape)


