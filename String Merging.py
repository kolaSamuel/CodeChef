def simplify(S):
    result = [S[0]]
    for i in xrange(1,len(S)):
        if S[i] == result[-1]: continue
        result.append(S[i])
    return result
    
for _ in xrange(input()):
    N,M = map(int,raw_input().strip().split())
    A = simplify(raw_input().strip())
    B = simplify(raw_input().strip())
    #initialize
    N,M = len(A),len(B)
    arr = [[N+M]*(N+1) for _ in xrange(M+1)]#count
    #maximum subsequece problem
    for i in xrange(1,M+1):
        for j in xrange(N):
            if B[i-1] == A[j]:
                arr[i][j] = arr[i-1][j-1] -1 #update
            else:
                count = arr[i-1][j]
                _count= arr[i][j-1]
                if count < _count:
                    arr[i][j] = count
                else:
                    arr[i][j] = _count
    print min(arr[-1])
    
