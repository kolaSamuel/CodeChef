t = input()

for i in xrange(t):
    c = map(str,raw_input())
    ans = 0 if c[0] == 'U' else 1
    for j in xrange(1,len(c)):
        if c[j-1] == 'U' and c[j] == 'D':ans+=1
    ans1 = 0 if c[0] == 'D' else 1
    for j in xrange(1,len(c)):
        if c[j-1] == 'D' and c[j] == 'U':ans1+=1
    print min(ans,ans1)
