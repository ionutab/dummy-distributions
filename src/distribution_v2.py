import random
from math import floor, ceil
import sys

from utils import diff_until, max_delta

def get_distribution(t, n):
    pauses = [0] * n
    avg = t / n
    delta = avg
    for i in range(0, n):
        # print("i %s" % i)
        # print("delta %s" % delta)
        if i < n - 1:
            r = random.uniform(0, delta * max_delta(i, n))
            # print("r %s" % r)
            pauses[i] = r
            if avg < r:
                delta = avg - diff_until(r, avg)
            if avg > r:
                delta = avg + diff_until(avg, r)
        else:
            pauses[i] = t - sum(pauses)
            # total = sum_array(pauses)
            # if total < t:
            #     pauses[i] = t - total
            # else:
            #     pauses[i] = 0
        # print(pauses)
    return pauses

t = int(sys.argv[1])
n = int(sys.argv[2])

print("Hello distribution v2 %s %s" % (t, n))
for i in range(0, 10):
    distribution = get_distribution(t, n)
    print(distribution)
    print(sum(distribution))



