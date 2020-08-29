# Snowflake

[![Build Status](https://travis-ci.org/trongbq/snowflake.svg?branch=master)](https://travis-ci.org/trongbq/snowflake)

A sequence generator based on the idea of [Twitter Snowflake](https://blog.twitter.com/engineering/en_us/a/2010/announcing-snowflake.html).
Other python libraries I found are either using Python2 or unstable due to not solving `clock drift`
issues.

### Environment
Library is designed and run on Python >= 3.8

### Structure

```
+------------------------------------------------------------------------+
| 1 Bit Unused | 41 Bit Timestamp |  10 Bit Node ID  |   12 Bit Sequence |
+------------------------------------------------------------------------+
```

### Example

```python
>>> from snowflake import Snowflake
>>> s = Snowflake(1)
>>> s.next_id()
6705036940686659584
>>> s.next_id()
6705036940690853888
>>> s.next_id()
6705036940699242496
```

### Benchmark

Library's benchmark result from `benchmark.py` file.
```
Benchmark on 10 IDs within 15606 nanoseconds (0.015606 millis), each ID took 1560.6 nanoseconds
Benchmark on 100 IDs within 122336 nanoseconds (0.122336 millis), each ID took 1223.36 nanoseconds
Benchmark on 1000 IDs within 1228141 nanoseconds (1.228141 millis), each ID took 1228.141 nanoseconds
Benchmark on 10000 IDs within 11263438 nanoseconds (11.263438 millis), each ID took 1126.3438 nanoseconds
Benchmark on 1000000 IDs within 1134503695 nanoseconds (1134.503695 millis), each ID took 1134.503695 nanoseconds
```
