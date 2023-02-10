# a > b
def diff_until(a, b):
    diff = a - b
    while diff > b:
        diff = diff - b
    return diff

def max_delta(i, n):
    return (n + (n - i + 1)) / n  