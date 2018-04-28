for _ in xrange(input()):
    l = input()
    A = raw_input().strip().split()
    B = A[:]
    for i in xrange(l):
        if B[i]==A[i]:
            for j in xrange(l):
                if B[j] != B[i] and  A[j] != B[i]:
                    B[i],B[j] = B[j],B[i]
                    break
    print reduce(lambda y,x: y + (B[x]!=A[x]),xrange(l),0)
    print " ".join(B)
            
##for _ in xrange(input()):
##    singles = set()
##    doubles = set()
##    ham = 0
##    l = input()
##    A = raw_input().strip().split()
##    B = A[:]
##    for x in A:
##        if x in singles:
##            doubles.add(x)
##        else:
##            singles.add(x)
##    if len(doubles) == len(singles):
##        dd = True
##    for i in xrange(l):
##        val = A[i]
##        for x in doubles:
##            if val != x:
##                B[i] = x
##                if x in singles:
##                    singles.remove(x)
##                else:
##                    doubles.remove(x)
##                ham+=1
##                break
##        if B[i] == val:
##            for x in singles:
##                if val != x:
##                    B[i] = x
##                    singles.remove(x)
##                    ham+=1
##                    break
##    try:
##        if B[-2] == A[-2]:
##            x = -2
##        else:
##            x = -1
##    except:
##        x = -1
##    if B[x] == A[x]:
##        try:
##            val = singles.pop()
##        except:
##            val = doubles.pop()         
##        for i in xrange(l):
##            if B[i] != val and  A[i] != val:
##                B[x],B[i] = B[i],val
##                ham+=1
##                break     
##    print ham
##    print " ".join(B) if l<4 or ham == l else c[23]
