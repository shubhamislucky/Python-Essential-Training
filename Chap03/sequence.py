#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5]
for i in x:
    print('i is {}'.format(i))

print(len(x))

y = [x for x in range(1,6)]
print(y)

z = list(range(5))
print(z)

dic = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for i,v in dic.items():
    print(i, v)
for x in dic.values():
    print(x)
for x in dic.keys():
    print(x)

# working with tuples
newtuple = (1, 3, 5, 'hello', 'there', [1, 2, 3, 4, 5])
sectuple = (1, 3, 5, 'hello', 'there', [1, 2, 3, 4, 5])
print(newtuple)
print(type(newtuple))
print(id(newtuple))
print(id(sectuple))

if newtuple is sectuple:
    print("They are the same")
else:
    print("They are different")

# this is because they both are pointing to different objects
print(f"id of newtuple {id(newtuple)} is not same as id of sectuple {id(sectuple)}")

# this is because they both are pointing to the same object
print(f"id of '1' in newtuple {id(newtuple[0])} is same as id of '1' in sectuple {id(sectuple[0])}")


if isinstance(newtuple, tuple):
    print("hello world")

if isinstance(newtuple[5], list):
    print("There is a list at index 5 in tuple 'newtuple'.")