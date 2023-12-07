# Project Euler - Problem 206

# "Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit."

from math import sqrt

digits = '1234567890'


def desired(x):
    return digits == str(x)[::2]


largest = 1929394959697989990
smallest = 1020304050607080900
largestroot = int(sqrt(largest))
smallestroot = int(sqrt(smallest))
print(f'{largestroot:,}, {smallestroot:,}')
print(desired(smallest))
for root in range(smallestroot, largestroot, 10):
    if desired(root**2):
        break
print(root**2, root)
