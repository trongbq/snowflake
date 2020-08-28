import unittest

import snowflake
from snowflake import Snowflake


class TestSnowflake(unittest.TestCase):
    def test_constructor_invalid_node_min(self):
        invalid_node = -1
        with self.assertRaises(AssertionError):
            s = Snowflake(invalid_node)


    def test_constructor_invalid_node_max(self):
        invalid_node = snowflake.NODE_MAX_VALUE + 1
        with self.assertRaises(AssertionError):
            s = Snowflake(invalid_node)

    def test_next_id(self):
        now = lambda: 0
        node = 1
        s = Snowflake(node, now)
        expected = snowflake.ORIGIN_EPOCH << snowflake.TIMESTAMP_LEFT_SHIFT | node << snowflake.NODE_LEFT_SHIFT | 0
        next_id = s.next_id()
        self.assertEqual(next_id, expected)


if __name__ == '__main__':
    unittest.main()

