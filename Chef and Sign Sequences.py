t = input()
for i in xrange(t):
    s = raw_input()
    ans = 0;state = 0
    #print s
    for j in s:
        if j == '>':
            state+=1
            ans = max(state,ans)
        elif j == '<':
            if state == 0 :ans+=1
            else:state-=1
    print ans+1 if ans > 1 else 0
