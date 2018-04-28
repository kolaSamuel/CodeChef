lim = 2*10**6+2
def totalroomD(x):
    num = [0,0]
    while x:
        toAdd = x%10
        num[toAdd&1]+=toAdd
        x/=10
    return abs(num[0]-num[1])
diamonds = map(totalroomD,xrange(lim))
for i in xrange(1,lim):
    diamonds[i]+=diamonds[i-1]
memo = [0]*(lim/2)
for i in xrange(1,lim/2):
    memo[i] = memo[i-1]+diamonds[2*i-1]+diamonds[2*i]-2*diamonds[i]    
for _ in xrange(input()):
    print memo[input()]
