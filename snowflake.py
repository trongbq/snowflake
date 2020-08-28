import time
from typing import Final, Callable
import logging


NODE_BIT: Final = 10
NODE_MAX_VALUE: Final = -1 ^ (-1 << NODE_BIT)
NODE_LEFT_SHIFT: Final = 12
SEQUENCE_BIT: Final = 12
SEQUENCE_BIT_MASK = -1 ^ (-1 << SEQUENCE_BIT)
TIMESTAMP_LEFT_SHIFT: Final = NODE_BIT + SEQUENCE_BIT
# Since time#monotonic only return distance time, so using this milestone epoch as an origin
ORIGIN_EPOCH = int(time.time() * 1000)

log = logging.getLogger(__name__)


class Snowflake:
    '''
    An ID generator based on Twitter Snowflake idea
    The structure:
        +------------------------------------------------------------------------+
        | 1 Bit Unused | 41 Bit Timestamp |  10 Bit Node ID  |   12 Bit Sequence |
        +------------------------------------------------------------------------+
    '''

    def __init__(self, node_id: int, now: Callable[[], int] = lambda: int(time.monotonic())):
        assert node_id >= 1 and node_id <= NODE_MAX_VALUE
        self.node_id = node_id
        self.last_timestamp = -1
        self.sequence = 0
        self.now = now


    def next_id(self) -> int:
        timestamp = self.now()

        if timestamp < self.last_timestamp:
            log.warning("Clock is moving backwards, current timestamp: " + str(timestamp) + " - last timestamp: " + str(self.last_timestamp))
            raise SystemError("Clock is moving backwards!!!")

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & SEQUENCE_BIT_MASK
            if self.sequence == 0:
                #  Out of sequence value, wait for the next millis
                timestamp = nextMillis()
        else:
            self.sequence = 0

        self.last_timestamp = timestamp

        return (timestamp + ORIGIN_EPOCH) << TIMESTAMP_LEFT_SHIFT | self.node_id << NODE_LEFT_SHIFT | self.sequence


    def next_millis(self) -> int:
        timestamp = self.now()
        while timestamp == self.last_timestamp:
            timestamp = self.now()
        return timestamp

