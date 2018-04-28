##from collections import defaultdict
##for _ in xrange(input()):
##    string = list(raw_input().strip(' '))
##    seen = defaultdict(set)
##    l = len(string)
##    yes = False
##    for i in xrange(l):
##        start = string[i]
##        for j in xrange(i+1,l):
##            end = string[j]
##            val = start+end
##            #print val,i,j,seen
##            if val in seen:
##                if not(i in seen[val] or j in seen[val]):
##                    #print val
##                    yes = True
##                    break
##            else:
##                seen[val].add(i)
##                seen[val].add(j)
##        if yes:break
##    print 'yes' if yes else 'no'
from collections import Counter
for _ in xrange(input()):
    string = raw_input().strip('')
    a = Counter(string)
    yes = False
    if any(x >1 for x in a.values()):yes = True
    print 'yes' if yes else 'no'
