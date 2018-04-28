from math import ceil
for i in xrange(input()):
    n = input()
    A = sorted(range(1,n+1), key = lambda x: x%2 +ceil(x/2.0))
    if n%2:
        A[-1],A[-2] =A[-2],A[-1]
    print " ".join(str(x) for x in A)
    
