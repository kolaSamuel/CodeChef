def fill(A,ins):
    """ helper function of mainFill"""
    
    def mainFill(A,ins):
        l = len(ins)
        discard = []
        violated = False
        for _ in xrange(l):
            i,j,x = ins[_]
            if A[i] == None and A[j] == None:
                discard.append((i,j,x))
            elif A[i] == None:
                A[i] = abs(A[j]-x)
            elif A[j] == None:
                A[j] = abs(A[i]-x)
            elif x != abs(A[i] - A[j]):
                violated = True
        if violated:
            return violated
        elif l > len(discard):
            return mainFill(A,discard)
        elif len(discard)==0:
            return violated
        else:
            A[i] = 0
            return mainFill(A,discard)
        
    i,j,x = ins[0]
    A[i] = 0
    violated = mainFill(A,ins)
    
    return violated  

for _ in xrange(input()):
    N,Q = map(int,raw_input().split(' '))
    A =[None]*(N+1)
    violated = False
    ins = [map(int,raw_input().split(' ')) for __ in xrange(Q)]
    
    print 'no' if fill(A,ins) else 'yes'
