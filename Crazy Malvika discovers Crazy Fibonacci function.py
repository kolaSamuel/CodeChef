t = input()
for i in xrange(t):
    a,b,n = map(int,raw_input().split())
    f = [];c = 3
    f.append(a);f.append(b)
    fi = lambda x: f[x-2]-f[x-3]
    while len(f) < n :
        f.append(fi(c));c+=1
    print f[-1]%(7+10**9)
        
