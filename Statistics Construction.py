for _ in xrange(input()):
    n = input()
    a = n/2
    if n%2:
        print " ".join(str(x) for x in xrange(n-a,n+a+1))
    else:
        print " ".join(str(x) for x in xrange(n-a,n+a))
