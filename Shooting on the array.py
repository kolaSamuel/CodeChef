from bisect import bisect_left
class skipSearch(object):
    """Searches through next maximum element in an array
    """
    def __init__(self,A):
        self.A = A
        self.next_i = [None]*len(A)
        for i in xrange(len(A)-2,-1,-1):
            self.nextMax(A[i],i+1)
        #print self.next_i
            
    def nextMax(self,x,i):
        j = i
        while 1:
            if j == None:
                break
            elif x >= self.A[j]:
                j = self.next_i[j]
            else:
                self.next_i[i-1]= j
                break

    def shot(self,i,L,R):
        result = 0
        while 1:
            if i == None:
                break
            elif L > self.A[i]:
                i = self.next_i[i] 
            elif R > self.A[i]:
                result+=1
                i = self.next_i[i]
            else:
                result+=1
                break
        print result
        
for _ in xrange(input()):
    N,Q = map(int,raw_input().strip().split())
    A = skipSearch(map(int,raw_input().strip().split()))
    
    for __ in xrange(Q):
        temp = raw_input().strip().split()
        if temp[0] == '+':
            continue
            i = int(temp[1])
            x = int(temp[2])
            A[i-1] += x
            maxToEnd.update(x,i)
        else:
            i,L,R = map(int,temp[1:])
            i-=1
            L-=0.5
            R-=0.5
            A.shot(i,L,R)
