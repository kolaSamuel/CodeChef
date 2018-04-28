##class node(object):
##    def __init__(self,parent = None,leftChild = None,rightChild = None):
##        self.data = 0
##        self.parent = parent
##        self.left = leftChild
##        self.right = rightChild
##        
##    def setValue(self,x):
##        self.data = x
##        
##class segment(object):
##    def __init__(self,arr):
##        self.root = node()

N,Q = map(int,raw_input().split())
A = map(int,raw_input().split())
_A = A[:]
_A.append(0)
for i in xrange(1,N):
    _A[i] ^= _A[i-1]
for _ in xrange(Q):
    t,i,k = map(int,raw_input().split())
    if t == 1:
        i-=1
        A[i]=k
        for j in xrange(i,N):
            _A[j] = A[j]^_A[j-1]
    else:
        print reduce(lambda y,x:y+(_A[x]==k),xrange(i),0)
