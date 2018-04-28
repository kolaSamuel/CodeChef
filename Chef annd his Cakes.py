for _ in xrange(input()):
    N,M = map(int,raw_input().strip().split())
    pattern = 'RG'
    cost = [3,5]
    R_G = [0,0] 
    for i in xrange(N):
        start = i&1
        for x in raw_input().strip():
            if x != pattern[start]:
                R_G[0]+=cost[start]
            else:
                R_G[1]+=cost[not(start)]
            start = not(start)
    print min(R_G)
