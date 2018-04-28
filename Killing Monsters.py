##from random import randint
##while 1:
N = input()#randint(1,16)#
h = map(int,raw_input().strip().split())#[randint(1,30) for _ in xrange(N)]#
seg = min(17,len(bin(N))-2)
lim = 2**(seg)
q = input()#N#
querry = [map(int,raw_input().strip().split()) for _ in xrange(q)]#[[randint(1,30),randint(1,30)] for _ in xrange(N)]#
ans = [0]*q
div = 1000
for i in xrange(0,q,div):
    block = [0]*lim
    j = min(i+div,q)

    for k in xrange(i,j):
        x,y = querry[k]
        x &= lim-1
        block[x]+=y
    #SOS DP modification
    for slide in xrange(seg):
        for mask in xrange(lim-1,-1,-1):
            if not ((1<<slide)&mask):
                block[mask] += block[(1<<slide)^mask]

    for monster in xrange(N):
        if h[monster] == 0:
            continue
        if h[monster] > block[monster]:
            h[monster]-=block[monster]
        else:
            for k in xrange(i,j):
                x,y = querry[k]
                if x & monster == monster:
                    h[monster]-=y
                    if h[monster] <= 0:
                        ans[k]-=1
                        break
sub = 0
for i in xrange(q):
    sub+=ans[i]
    print N+sub     
