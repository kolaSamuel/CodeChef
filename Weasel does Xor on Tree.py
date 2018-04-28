from collections import defaultdict,Counter

class tree(object):
    #"""A tree!!!!!!, might need a node class to optimize tho"""
    def __init__(self):
        self.tree = defaultdict(list)
        
        #first element of each node is its parent other values
        #are its children
        self.tree[0].append('Root')
        self.values = []
        self.days = Counter()
        self.repeat = 0
        self.length = 0
        self.states = {}

    def insert(self,u,v):
        #assumes u is already in tree and adds v to children
        self.tree[u].append(v)
        #sets the parent of v to u
        self.tree[v].append(u)
        
        #updates all parents of u to have the child v
        parent = self.tree[u][0]
        while parent != 'Root':
            self.tree[parent].append(v)
            parent = self.tree[parent][0]

    def solve(self,x):
        l = len(self.values)
        for i in xrange(x+1):
            #_days = Counter()
            visited = str(self.values)
            if visited in self.states:
                break
            self.states[visited]=i
            self.days[i] = self.values[0]
            for j in xrange(l):
                children = self.tree[j][1:]
                for y in children:
                    self.values[j]^=self.values[y]
            #self.values = _days
            
    def setValues(self,A):
        self.values = A

    def getDay(self,x):
        return self.days[x]

N,Q = map(int,raw_input().split(' '))
wTree = tree()

for _ in xrange(N-1):
    u,v = map(int,raw_input().split(' '))
    wTree.insert(u,v)
    
A = map(int,raw_input().split(' '))
wTree.setValues(A)

days =[None]*Q
mx = 0
for i in xrange(Q):
    day = input()
    days[i]=day
    mx = max(mx,day)
## runtime error????
if mx < 10**7:
    wTree.solve(mx)
for x in days:
    print wTree.getDay(x)
