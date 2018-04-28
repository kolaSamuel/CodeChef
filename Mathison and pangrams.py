from collections import Counter
az = Counter(list('qwertyuiopasdfghjklzxcvbnm'))
for _ in xrange(input()):
    cost = map(int,raw_input().split(' '))
    word = Counter(list(raw_input()))
    left = az-word
    tCost = 0
    for key in left:
        tCost+= cost[ord(key)-97]
    print tCost
