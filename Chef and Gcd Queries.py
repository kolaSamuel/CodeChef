from collections import Counter
from fractions import gcd

lim = 10**5 + 1
segment = 320
primes = []
numbers = range(lim)
numbers[1] = 0
for i in xrange(2, lim):
    if numbers[i]:
        primes.append(i)
        for j in xrange(2*i, lim, i):
            numbers[j] = 0

n = input()
arr = map(int, raw_input().split()) # can be optimized with Counter
results = [Counter() for _ in xrange((n//segment) + 1)]


def prime_factors(x, factors, i=0):
    if numbers[x]:
        factors.append(x)
    elif x > 1:
        y = primes[i]
        while x % y:
            i += 1
            y = primes[i]
        while x % y == 0:
            x /= y
            factors.append(y)
        prime_factors(x, factors, i+1)


def power_set(factors):

    result = set()
    for x in factors:
        for y in list(result):
            result.add(y*x)
        result.add(x)

    return result


def query_one(index, to_add=1):
    pos = n // segment
    val = arr[index]
    factors = []
    prime_factors(val, factors)
    for effect in power_set(factors):
        results[pos][effect] += to_add


for i in xrange(n):
    query_one(i)

for _ in xrange(input()):
    query = map(int, raw_input().split())
    # print results
    if query[0] == 1:
        x, y = query[1]-1, query[2]
        query_one(x, -1)
        arr[x] = y
        query_one(x)
    else:
        q, left, right, x = query
        left -= 1
        right -= 1
        answer = 0
        for i in xrange(len(results)):
            pos = i*segment
            if left <= pos and right >= pos+segment-1:
                answer += segment - results[i][x]
            elif right < pos:
                break
            else:
                start = max(pos, left)
                end = min(pos+segment-1, right)
                for j in xrange(start, end+1):
                    if gcd(arr[j], x) == 1:
                        answer += 1
        print answer
