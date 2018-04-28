from bisect import bisect_left
for _ in xrange(input()):
    N = input()
    arr = [sorted(map(int,raw_input().strip().split())) for _ in xrange(N)]
    result = _max = arr[-1][-1]
    for i in xrange(2,N+1):
        index = bisect_left(arr[-i],_max) - 1
        if index == -1:
            print -1
            break
        _max = arr[-i][index]
        result+=_max
    else:
        print result
