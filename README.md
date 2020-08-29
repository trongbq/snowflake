Snowflake

A sequence generator based on the idea of [Twitter Snowflake](https://blog.twitter.com/engineering/en_us/a/2010/announcing-snowflake.html).
Other python libraries I found are either using Python2 or unstable due to not solve `clock drift`
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
TBD

