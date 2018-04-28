for _ in xrange(input()):
    rec = map(int,raw_input().strip().split())
    print 'NO' if any(rec.count(x)&1 for x in rec) else 'YES'
