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
        outer = 0
        now = lambda: outer
        node = 1
        s = Snowflake(node, now)

        expected = snowflake.ORIGIN << snowflake.TIMESTAMP_LEFT_SHIFT | node << snowflake.NODE_LEFT_SHIFT | 0
        next_id = s.next_id()
        self.assertEqual(next_id, expected)

        #  Verify that with same timestamp, sequence is increased by 1
        expected = snowflake.ORIGIN << snowflake.TIMESTAMP_LEFT_SHIFT | node << snowflake.NODE_LEFT_SHIFT | 1
        next_id = s.next_id()
        self.assertEqual(next_id, expected)

        #  Verify that on next timestamp, sequence is reset to 0
        outer = 1
        expected = snowflake.ORIGIN + 1 << snowflake.TIMESTAMP_LEFT_SHIFT | node << snowflake.NODE_LEFT_SHIFT | 0
        next_id = s.next_id()
        self.assertEqual(next_id, expected)

    #  def test_next_id_next_millis(self):
    #      outer = 0
    #      now = lambda: outer
    #      node = 1
    #      s = Snowflake(node, now)

    #      #  Use all available sequence for a timestamp
    #      for i in range(snowflake.SEQUENCE_BIT_MASK + 1):
            #  s.next_id()

    def test_decompose(self):
        now = lambda: 1
        s = Snowflake(999, now)
        next_id = s.next_id()
        (timestamp, node_id, seq) = s.decompose(next_id)

        self.assertEqual(seq, 0)
        self.assertEqual(node_id, 999)
        self.assertEqual(timestamp, snowflake.ORIGIN + snowflake.TIMESTAMP_EPOCH + 1)


if __name__ == '__main__':
    unittest.main()

