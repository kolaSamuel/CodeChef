def teleportGame(r,c,n,T,board,s):
    """Runs a breadth frist search,nothing special here
    """
    fringe = []
    #start state
    node = [s,T,board[s[0]][s[1]]]
    best = 0
    while 1:
        #goal check
        if node[2]>best:best = node[2]
        fringe+=getSuccessors(node,board,r,c)
        if len(fringe):
            node = fringe.pop(0)
        else:return best
        
def getSuccessors(node,board,r,c):
    """ gets current node, board confuguration, row length and column length
        and gets successors given the current available teleportions available
        in T (node[1]).
    """
    s,T,score = node
    successors = []
    for i in xrange(len(T)):
        #Generates all combinations for the teleport pad given
        for x in [-1,1]:
            for y in [-1,1]:
                _x = s[0]+ x*T[i][0]
                _y = s[1]+ y*T[i][1]
                if _x <= r and _y <= c:
                    if _x >= 0 and _y >=0:
                        _score = score+ board[_x][_y]
                        successors.append([(_x,_y),T[:i]+T[i+1:],_score])
    return successors

for _ in xrange(input()):
    R,C,N = map(int,raw_input().split(' '))
    _T,T = [],[]
    start = map(int,raw_input().split(' '))
    for __ in xrange(2):
        _T.append(map(int,raw_input().split(' ')))
    for i in xrange(N):T.append((_T[0][i],_T[1][i]))
    board = []
    for ___ in xrange(R):
        row = map(int,raw_input().split(' '))
        board.append(row)
    print teleportGame(R-1,C-1,N,T,board,start)
    
