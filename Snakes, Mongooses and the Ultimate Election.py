t = input()
for i in xrange(t):
    v = list(raw_input())
    s = v.count('s')
    m = v.count('m')
    for j in xrange(1,len(v)):
        if v[j] == 'm':
            if v[j-1] == 's':
                s-=1;v[j-1] = '-'
            elif v[j+1] == 's':
                s-=1;v[j+1] = '-'
    if s == m:print 'tie'
    else:print 'snakes' if s>m else 'mongooses'
