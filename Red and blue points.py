from collections import Counter
class fenwick(object):
    def __init__(self):
        self._max = 2*10**9+2
        self.tree = Counter()

    def update(self,i):
        while i < self._max:
            self.tree[i]+= 1
            i+=i&(-i)

    def __getitem__(self,y):
        result = 0
        while y:
            result += self.tree[y]
            y-=y&(-y)
        return result
    
def scan(red,blue,lines,result,N,M):
    for line in lines:
        x = line+1
        y = line-1
        if not (x in lines):
            RED = red[x]
            BLUE = blue[x]
            result = min(result,RED+M-BLUE,BLUE+N-RED)
        if not (y in lines):
            RED = red[y]
            BLUE = blue[y]
            result = min(result,RED+M-BLUE,BLUE+N-RED)
        RED = red[line]
        BLUE = blue[line]
        onLine = RED-red[y]+BLUE-blue[y]
        result = min(result,RED+M-BLUE+onLine,BLUE+N-RED+onLine)
    return result

for _ in xrange(input()):
    lim = 10**9+1
    N,M = map(int,raw_input().strip().split())
    rowScan = set()
    colScan = set()
    redRow = fenwick()
    blueRow = fenwick()
    redCol = fenwick()
    blueCol = fenwick()
    for i in xrange(N):
        row,col = map(lambda x:int(x)+lim,raw_input().strip().split())
        rowScan.add(row)
        colScan.add(col)
        redRow.update(row)
        redCol.update(col)
    for i in xrange(M):
        row,col = map(lambda x:int(x)+lim,raw_input().strip().split())
        rowScan.add(row)
        colScan.add(col)
        blueRow.update(row)
        blueCol.update(col)
    print min(scan(redRow,blueRow,rowScan,'a',N,M),scan(redCol,blueCol,colScan,'a',N,M))
