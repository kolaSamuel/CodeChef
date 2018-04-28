for _ in xrange(input()):
    N,K = map(int,raw_input().strip().split())
    S = set(map(int,raw_input().strip().split()))
    for i in xrange(1+2*10**5):
        if i in S:continue
        if K == 0:
            break
        else:
            K-=1
    print K+i
