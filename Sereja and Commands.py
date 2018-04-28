mod = 7+10**9
class fenwick(object):
    def __init__(self,length):
        self.tree = [0]*(length+1)
        self.length = length
        
    def update(self,l,r,x):
        mx = self.length
        while l <= mx:
            self.tree[l]+=x
            l = l+(l&(-l))
        r+=1
        while r <= mx:
            self.tree[r]-=x
            r = r+(r&(-r))
            
    def sumIndex(self,i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i = i -(i&(-i))
        return result

    def __str__(self):
        array = [self.sumIndex(i)%mod for i in xrange(1,self.length+1)]
        string = " ".join(str(x) for x in array)
        return string
    
for _ in xrange(input()):
    n,m = map(int,raw_input().split(' '))
    #stores t,l,r array in commands
    commands = [map(int,raw_input().split(' ')) for _i in xrange(m)]
    cmds = fenwick(m)
    cmds.update(1,m,1)
    A = fenwick(n)
    for i in xrange(m-1,-1,-1):
        t,l,r = commands[i]
        x = cmds.sumIndex(i+1)
        if t == 1:
            A.update(l,r,x)
        else:
            cmds.update(l,r,x)
    print A
