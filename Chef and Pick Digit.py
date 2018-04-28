from collections import Counter
from itertools import permutations
for _ in xrange(input()):
    n = raw_input()
    _A = Counter([int(x) for x in n])
    A = []
    for x in _A:
        A.append(x)
        if _A[x]-1:A.append(x)
    A.sort()
    result = []
    for i,j in permutations(A,2):
        val = int(str(i)+str(j))
        if val >64 and val < 91:result.append(val)
    answer = "".join(chr(x) for x in set(result))
    print answer
