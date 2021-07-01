
import unittest
from functools import reduce
from operator import mul
from pandas.testing import assert_frame_equal
import fast_views
from . import util

total_cells = lambda df: reduce(mul,df.shape)

class TestFastJoin(unittest.TestCase):
    def test_join_equal(self):
        a = util.time_unit_column_df("a",1, 0, 20)
        b = util.time_unit_column_df("b",1, 10, 30)
        assert_frame_equal(
                a.join(b,how="inner"),
                fast_views.inner_join([a,b])
                )
