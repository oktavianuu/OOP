from sys import path

path.append('../modules')

import modules

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(modules.sum1(zeroes))
print(modules.prod1(ones))
