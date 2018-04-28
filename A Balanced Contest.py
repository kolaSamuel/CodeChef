for _ in xrange(input()):
    N,P = map(int,raw_input().strip().split())
    cake = P/2
    hard = P/10
    c,h =0,0
    Q = map(int,raw_input().strip().split())
    for x in Q:
        if x >= cake:c+=1
        if x <= hard:h+=1
    print 'yes' if h == 2 and c == 1 else 'no'
