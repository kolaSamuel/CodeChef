def dfs(tree,v,k,f,sumArr,d,visited):
    visited.add(v)
    if d > k:
        return
    for x in tree[v]:
        if x in visited:
            continue
        if not( d in f):
            f[d] = f[d-1]+f[d-2]
        sumArr[x]+=f[d]
        dfs(tree,x,k,f,sumArr,d+1,visited)
    
mod = 10**9 +7
for _ in xrange(input()):
    N,Q = map(int,raw_input().strip().split())
    tree = [ [] for _ in xrange(N+1)]
    sumArr = [0]*(N+1)
    for _ in xrange(N-1):
        u,v = map(int,raw_input().strip().split())
        tree[u].append(v)
        tree[v].append(u)
    for _ in xrange(Q):
        temp = map(int,raw_input().strip().split())
        if temp[0] == 2:
            print sumArr[temp[1]]%mod
        else:
            t,v,k,a,b = temp
            f = {0:a,1:b}
            sumArr[v]+=a
            dfs(tree,v,k,f,sumArr,1,set())

