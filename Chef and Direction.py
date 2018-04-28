from itertools import combinations
from math import ceil
from copy import deepcopy as deep

def adjust(orders,i,N,left,speed = False):
    
    if speed:
        i-=1
    for j in xrange(i+1,N):
        d = orders[j][1]
        if left >= d:
            orders[j][1] = 0
            left -= d
        else:
            if speed:
                orders[j][0]-= (left/speed)
            orders[j][1] -= left
            left = 0
            break
    if speed:
        return i+2
    return left

def possible(orders,speeds,N):
    for i in xrange(N):
        time,d =orders[i]
        if d <= 0:
            continue
        k = i
        for speed in speeds:
            t1,d = orders[k]
            d1 = speed*t1
            if d1 < d:
                return False
            distance = speed*time
            k = adjust(orders,k,N,distance,speed)
            if k >= N:
                break   
    return True

for __ in xrange(input()):
    candidates = []
    K = input()
    for _ in xrange(K):
        P,S = map(int,raw_input().strip().split())
        candidates.append((P,S))
    costs = []
    select = range(K)
    for i in xrange(1,K+1):
        for x in combinations(select,i):
            dishes = 0
            cost = 0
            for y in x:
                dishes+=candidates[y][0]
                cost+=candidates[y][1]
            costs.append((cost,dishes,x))
    costs.sort()
    orders = []
    N = input()
    for _ in xrange(N):
        D,M = map(float,raw_input().strip().split())
        orders.append([M,D])
    orders.sort()
    _orders = deep(orders)
    speed = 1 #dishes per min
    time = 0 #initialize time

    for i in xrange(N):
        t,d = orders[i]
        if d < 1:
            continue
        distance = speed*(t-time)
        if distance >= d:
            time = t
            if adjust(orders,i,N,distance-d):
                break
        else:
            increase = ceil((d-distance)/t)
            speed+=increase
            time = t
    speed = int(speed)
    result = -1
    for (cost,dishes,comb) in costs:
        if dishes >= speed and len(comb) <= N:
            _max = max(candidates[x][0] for x in comb)
            _max_ = max(orders[x][1]/orders[x][0] for x in xrange(N))
            if _max >= _max_:
                result = cost
                break
##            speeds = [candidates[x][0] for x in comb]
##            speeds.sort(reverse = True)
##            if possible(deep(_orders),speeds,N):
##                result = cost
##                break
##            else:
##                print 'fail',__
##                print 'dishes',(cost,dishes,comb)
##                print 'speeds',speeds
##                print 'orders',_orders
##                print
    print result
