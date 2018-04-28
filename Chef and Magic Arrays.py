def dfs(n):
    global ingredents
    state = []
    pos=0
    fringe = []
    best = 0
    while 1:
        if pos == n:
            tasty = tastiness(state,n)
            if tasty > best:
                best =tasty
        else:
            for i in xrange(ingredents[pos]):
                fringe.append((state+[i],pos+1))
        if len(fringe)== 0:
            break
        else:
            state,pos =fringe.pop()
    return best

def tastiness(state,n):
    global ingredents
    global dishes  
    result = 0
    for i in xrange(n-1):
        lastIndex = ingredents[i]-state[i]-1
        firstIndex = 0-state[i+1]
        result+= (i+1)*abs(dishes[i][lastIndex]-dishes[i+1][firstIndex])
    return result

for _ in xrange(input()):
    n = input()
    dishes = []
    ingredents = []
    for __ in xrange(n):
        temp = map(int,raw_input().strip().split())
        dishes.append(temp[1:])
        ingredents.append(temp[0])
        
    print dfs(n)
