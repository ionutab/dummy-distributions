import random
import sys
import time
from math import floor, ceil

def get_distribution(t, n):
    pauses = [0] * n
    avg = t / n
    for i in range(0, n):
        if i < n - 1:
            r = random.uniform(0, avg * 2)
            pauses[i] = r
            avg = (t - sum(pauses)) / (n - i)
        else: 
            pauses[i] = t - sum(pauses)

    return pauses

t = int(sys.argv[1])
n = int(sys.argv[2])

print("Hello distribution v3 %s %s" % (t, n))
for i in range(0, 10):
    distribution = get_distribution(t, n)
    print(distribution)
    print(sum(distribution))



