''' Author: Tim Hung '''

# I want a data structure to store the different permutations of H and T
# But I want to maintain the order given
# An OrderedDict or ordered map will give me a fast lookup time and maintain order.
from collections import OrderedDict

num_cases = int(input())
for i in range(1, num_cases + 1, 1):
    # Each output line begins with the case number
    output = input() + ' '
    raw = input()

    # I define my permutations with the perm as the key
    # and the count as the value
    perms = OrderedDict()
    perms['TTT']= 0
    perms['TTH']= 0
    perms['THT']= 0
    perms['THH']= 0
    perms['HTT']= 0
    perms['HTH']= 0
    perms['HHT']= 0
    perms['HHH']= 0

    # Loop through the raw input until the 3rd to last elem
    for trip in range(0, len(raw)-2, 1):
        # Slice the raw input at the current index to get a substring of size 3
        # Increment its count!
        perms[raw[trip:trip+3]] += 1

    # Append the values to my output string with spaces delimiting
    # Remember that OrderedDict maintains the order the elems are initialized with
    for k, v in perms.items():
        output += str(v) + ' '

    print(output)
