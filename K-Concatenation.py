lim = -1000000
def kandane(A,sub = lim,F = lambda x,y: max(x,x+y)):
    _max = lim
    l = len(A)
    for i in xrange(l):
        sub = F(A[i],sub)
        _max = max(_max,sub)
    return _max
        
for _ in xrange(input()):
    N,K = map(int,raw_input().strip().split())
    A = map(int,raw_input().strip().split())
    _sum = sum(A)*(K-1)
    _sumAgain = 0 if K < 3 else sum(A)*(K-2)
    bestOne = kandane(A)
    forward = kandane(A,0,lambda x,y: x+y)
    A.reverse()
    reverse = kandane(A,0,lambda x,y: x+y)
    #compute all possibilities)
    if K == 1:
        print bestOne
    else:
        print max(reverse+_sum,reverse+forward,bestOne,reverse+forward+_sumAgain)
