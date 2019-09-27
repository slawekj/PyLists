import sys
import ast
import numpy

N = 10000

raw_input = sys.stdin.read()

list = ast.literal_eval(raw_input)

assert numpy.shape(list) == (N, N + 2), "List should be exactly %d by %d" % (N, N + 2)

assert map(lambda x: x[0], list) == range(0, N), "List should be indexed properly from 0 to %d" % (N - 1)

assert min(map(lambda x: min(x[1:-1]), list)) >= 0, "Minimum random number in a list must be greater or equal than 0"

assert max(map(lambda x: max(x[1:-1]), list)) < 10, "Maximum random number in a list must be lower than 10"

assert map(lambda x: sum(filter(lambda y: y > 3, x[1:-1])), list) == map(lambda x: x[-1], list), \
    "The last element in a list must be a sum of elements greater than 3"

print("homework is correct")
