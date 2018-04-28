t = input()
for i in xrange(t):
    n = input()
    ans = []
    for j in xrange(1,n):
        ans.append((j,j+1))
    ans.append((1,n))
    print n
    for k in xrange(n):
        print n
        for l in xrange(1,n+1):
            print l,ans[(k+l)%n][0],ans[(k+l)%n][1]
