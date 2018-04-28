for _ in xrange(input()):
    x,N = map(int,raw_input().strip().split())
    _sum = (N*(N+1))/2
    if N < 4 or (_sum&1)^(x&1):
        print 'impossible'
    else:
        arr = [0]*N
        arr[x-1] = 2
        A,B = 0,0
        for i in xrange(N,0,-1):
            if i == x:continue
            if A <= B:
                A+=i
            else:
                B+=i
                arr[i-1] = 1
        if A != B:
            arr[-1],arr[-2] = arr[-2],arr[-1]
        print "".join(map(str,arr))
