from math import sqrt
from random import sample,randint
def euclid(pos1,pos2 = (0,0)):
    if pos1 == pos2 or pos1 == None:
        return float('inf')
    x,y = pos1
    x1,y1 = pos2
    distance = (x-x1)**2 +(y-y1)**2
    distance = sqrt(distance)
    return distance

for _ in xrange(input()):
    N,G,B,X,Y = map(int,raw_input().strip().split())
    volume = map(int,raw_input().strip().split())
    want = [ set() for _ in xrange(G+1)]
    got = [0]*(N+1)
    coord = [(0,0)]
    wants = [0]*(N+1)
    for i in xrange(N):
        x,y,k,l = map(int,raw_input().strip().split())
        want[l].add(i+1)
        got[i+1] = k
        wants[i+1] = l
        coord.append((x,y))
    _min = randint(1,N)
    print 2,wants[_min]
    bag = wants[_min]
    space = volume[bag-1]
    loc = 0
    for _ in xrange(N):
        try:
            assert len(want[bag]) > 0
            _min = sample(want[bag],1)[0]
            loc = _min
            want[bag].remove(_min)
            coord[_min]= None
        except:
            print 1,0
            print 3,bag
            for i in xrange(G+1):
                if len(want[i])>0:
                    loc = want[i].pop()
                    bag = i
                    print 2,bag
                    break
        print 1,loc
        print 3,bag
        bag = got[loc]
        print 2,bag
    print 1,0
    print 0
