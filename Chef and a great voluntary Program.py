from collections import Counter
from fractions import gcd
def getRatio(x,y):
    if y == 0:
        return 'a'
    return (x*1.0/y)

def adjust(fruits,xy,last):
    string = ''
    x,y = xy
    f = ['a','b']
    add = False
    ratio = getRatio(fruits['a'],fruits['b'])
    if ratio > x*1.0/y:add = False #can be removed
    elif ratio < x*1.0/y:add = True
    else:
        #print 'ratio found',last,add
        if last[add]:add = not(add)
        div = gcd(x,y)
        x/=div
        y/=div
        xy=(x,y)
        string = f[add]*xy[add]+f[not(add)]*xy[not(add)]
        string*= fruits['a']/x#can be fruits['b']/y
        fruits['a']=0
        fruits['b']=0
        return string

    if fruits[f[add]] == 0: add = not(add)
    if last[add] >= xy[add]:
        if fruits[f[not(add)]]:add = not(add)
        else:
            string='*'+f[add]*xy[add]
            string*=fruits[f[add]]/xy[add]
            fruits[f[add]]%=xy[add]
            if fruits[f[add]]:
                string+='*'+f[add]*fruits[f[add]]
            fruits[f[add]]=0
            #print 'impossible to find ratio',string
            return string
    #print 'added',f[add],'from conditions',fruits,xy,last,'ratio: ',ratio
    string+= f[add]
    last[add]+=1
    last[not(add)]=0
    fruits[f[add]]-=1
    return string
 
for _ in xrange(input()):
    fruits = Counter(raw_input().strip())
    x,y = map(int,raw_input().strip().split())
    feed = ''
    length = fruits['b']+fruits['a']
    last = [0,0]
    while fruits['a'] or fruits['b']:
        feed += adjust(fruits,(x,y),last)
    print feed
