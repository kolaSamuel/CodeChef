t = input()
for i in xrange(t):
    n,d = map(int,raw_input().split())
    dy = [10**5]*d
    for j in xrange(n):
        di,ti,si = map(int,raw_input().split())
        for k in xrange(d-di):
            
