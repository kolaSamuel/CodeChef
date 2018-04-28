#from random import randint
def bestBC(arr):
    end = arr[:3]
    end.sort()
    A,B,C = arr[3:]
    MIN = min(end)
    _max = MIN
    _min = 0
    mid = (_max+_min)/2
    result = 'a'
    while 1:
        left = right = 'a'
        if _min == _max:
            break
        if mid > 0:
            end1 = [x-(mid-1) for x in end]
            left = bestB(end1,B,A)+(mid-1)*C
        if mid<MIN:
            end1 = [x-(mid+1) for x in end]
            right = bestB(end1,B,A)+(mid+1)*C
        end1 = [x-mid for x in end]
        centre = bestB(end1,B,A)+mid*C
        if left < right:
            _max = mid
        else:
            _min = mid+1
        result = min(result,centre,left,right)
            
        mid = (_max+_min)/2
    result = min(sum(end)*A,sum(end)*A+MIN*(C-3*A),result)
    return result

def bestB(end,B,A):
    firstTwo = end[0]+end[1]
    if firstTwo >= end[2]:
        total = firstTwo+ end[2]
        result = (total/2)*B + (total&1)*A
    else:
        result = firstTwo*(B-A)+end[2]*A
    return result

for _ in xrange(input()):
    temp = map(int,raw_input().strip().split())
    print bestBC(temp)
