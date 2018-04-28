for _ in xrange(input()):
    n = input()
    A = map(int,raw_input().split(' '))
    x = float('inf')
    for i in xrange(n):
        if A[i]<x:
            x = A[i]
            index = i
    print index+1
