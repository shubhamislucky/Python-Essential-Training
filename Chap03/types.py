#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
from decimal import *

x = 7
print('x is {}'.format(x))
print(type(x))
print("x is {1:<09} {0:>09}".format(8, 9))

a = 3
b = 4
print(f"hello values: {a:<9} {b:>9}")

# python doesn't work well with decimals as it sacrifices accuracy for precision
# so don't do money calculation with decimal like this instead use the other way
x = (0.1 + 0.1 + 0.1) - 0.3
print(x)

# use this way for decimal calculation
f = Decimal('.10')
s = Decimal('.30')
total = f + f + f - s
print(total)
