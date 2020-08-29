import time
from snowflake import Snowflake


def benchmark(n: int):
    s = Snowflake(1)
    start = time.monotonic_ns()
    i = 0
    while i < n:
        s.next_id()
        i += 1
    end = time.monotonic_ns()
    print('Benchmark on ' + str(n) + ' IDs within ' + str(end - start) + ' nanoseconds (' +
          str((end-start)/1000000) + ' millis), each ID took ' + str((end - start)/n) + ' nanoseconds')


if __name__ == '__main__':
    benchmark(10)
    benchmark(100)
    benchmark(1000)
    benchmark(10000)
    benchmark(1000000)
