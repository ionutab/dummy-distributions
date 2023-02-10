import random
import sys
import time
from math import floor, ceil

def get_distribution(t, n):
    pauses = [0] * n
    avg = t / n
    for i in range(0, n):
        pauses[i] = random.randint(floor(avg / 2), floor(avg - 1))
    return pauses


t = int(sys.argv[1])
n = int(sys.argv[2])

print("Hello distribution v1 %s %s" % (t, n))
for i in range(0, 10):
    distribution = get_distribution(t, n)
    print(distribution)
    total = sum(distribution)
    print(total)
    extra_wait = t - total
    print("plan %s -> %s -> %s" % (extra_wait / 2, total, extra_wait / 2))



