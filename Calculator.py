t = input()
for i in xrange(t):
    n,b = map(int,raw_input().split())
    r = n/b;st =r/2;mx = 0
    if r <= 1:print r*(n-b)
    else:
        mv = st
        while 1:#left
            m= mv*(n-mv*b)
            if m>mx:
                mx=m
                if mv==1:break
                mv-=1
            else:break
        mv = st+1
        while 1:#left
            m= mv*(n-mv*b)
            if m>mx:
                mx=m
                if mv==r:break
                mv+=1
            else:break
        print mx
