for _ in xrange(input()):
    a = input()
    arr = [1]*a
    val = 99998
    end = ((2**32)-a+1)/val
    arr[0]+=2**32-a-1+end - val*end
    for i in xrange(1,end):
        arr[i]=val
    print " ".join(str(x) for x in arr)
