S = raw_input().strip()
N = len(S)
tree = []
for i in xrange(1,N+1):
    for j in xrange(N-i+1):
        tree.append(S[j:j+i])
tree.sort()
string = ''.join(tree)

G = 0
for _ in xrange(input()):
    P,M = map(int,raw_input().strip().split())
    K = ((P%M)*(G%M))%M
    G+= ord(string[K])
    print string[K]
