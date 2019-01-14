#!/usr/bin/env python3

import timeit
import math


print("timeit_2<<number: ")
print(timeit.timeit('2<<number', setup='number=1000', number=10000))
print("timeit_2**number: ")
print(timeit.timeit('2**number', setup='number=1000', number=10000))
print("timeit_math.pow(2,number): ")
print(timeit.timeit('math.pow(2,number)', setup='import math; number=1000', number=10000))
print("timeit_pow(2,number): ")
print(timeit.timeit('pow(2,number)', setup='number=1000', number=10000))

print("timeit_for:")
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
print("timeit_compr:")
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))
print("timeit_map:")
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))
