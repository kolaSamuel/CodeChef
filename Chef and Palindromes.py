from collections import defaultdict
N = input()
white = map(int,raw_input().strip().split())
black = map(int,raw_input().strip().split())
magic = [0]*N
mixed = defaultdict(list)
result = [0]*N
for i in xrange(N):
    cast = white[i]-black[i]
    spell = ((cast+1)/2,cast/2)
    mixed[spell].append(i+1)

pot = None
i,j = 0,N-1

for x in mixed.keys():
    y = len(mixed[x])
    if y&1:
        mix = []
        for _ in xrange(y-1):
            mix.append(mixed[x].pop())
    else:
        mix = mixed.pop(x)
    y /= 2
    for k in xrange(y):
        result[i+k] = mix[k]
        result[j-k] = mix[y+k]
        magic[j-k] = 1
    i+=y
    j-=y
    
print result
print magic
print i,j
        
