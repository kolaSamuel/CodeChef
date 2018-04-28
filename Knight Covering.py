t = input()
def aSearch(b,n,m):
    fringe = []
    node = [0,b,0]
    while 1:
        ans = 0
        for i in xrange(n):
            ans+=sum(node[1][i])
        if ans == n*m :
            print node
            return node[2]
##        branch = getSuccessor(node,n,m)
##        for x in branch: fringe.append(x)
##        #print fringe
##        node = fringe.pop(fringe.index(max(fringe)))
##        #print node
        node = getSuccessor(node,n,m)
def getSuccessor(nod,n,m):
    state = list(nod[1])
    c = nod[2] + 1
    successor = []
    for i in xrange(n):
        for j in xrange(m):
            if state[i][j] == 0:
                nstate = []
                hueristic = nod[0]+1
                for x in state: nstate.append(list(x))
                nstate[i][j] = 1.0
                if j>1:
                    if i+1 < n:
                        if nstate[i+1][j-2]== 0:
                            nstate[i+1][j-2]=1;hueristic+=1
                    if i-1 >= 0:
                        if nstate[i-1][j-2]==0:
                            nstate[i-1][j-2]=1;hueristic+=1
                if m-j-1>1:
                    if i+1 < n:
                        if nstate[i+1][j+2]==0:
                            nstate[i+1][j+2]=1;hueristic+=1
                    if i-1 >= 0:
                        if nstate[i-1][j+2]==0:
                            nstate[i-1][j+2]=1;hueristic+=1
                if i>1:
                    if j+1 < m:
                        if nstate[i-2][j+1]==0:
                            nstate[i-2][j+1]=1;hueristic+=1
                    if j-1 >= 0:
                        if nstate[i-2][j-1]==0:
                            nstate[i-2][j-1]=1;hueristic+=1
                if n-i-1>1:
                    if j+1 < m:
                        if nstate[i+2][j+1]==0:
                            nstate[i+2][j+1]=1;hueristic+=1
                    if j-1 >= 0:
                        if nstate[i+2][j-1]==0:
                            nstate[i+2][j-1]=1;hueristic+=1
                successor.append([hueristic,nstate,c])
                        
                #if j == 2:print hueristic,nstate,c
    #print 'here',successor,state
    return successor.pop(successor.index(max(successor)))
for k in xrange(t):
    n,m = map(int,raw_input().split())
    b = []
    for l in xrange(n):
        b.append([0]*m)
    print aSearch(b,n,m)
