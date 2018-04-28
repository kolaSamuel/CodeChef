for _ in xrange(input()):
    N,K = map(int,raw_input().split(' '))
    posShift = 0
    for i in xrange(N,0,-1):
        if K%2:posShift+=(2**i)/2
        K//=2
    print K+posShift
