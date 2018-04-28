def penaltyShootOut(S):
    A_B = [0,0]
    for i in xrange(10):
        a = 5 -(i+2)/2
        b = 5 -(i+1)/2
        A_B[i&1]+=int(S[i])
        if A_B[0] > A_B[1]+b:return 'TEAM-A '+str(i+1)
        if A_B[1] > A_B[0]+a:return 'TEAM-B '+str(i+1)
    for i in xrange(10,21):
        j = i&1
        if not(j):
            if A_B[0]>A_B[1]:return 'TEAM-A '+str(i)
            A_B[j]+=int(S[i])
        else:
            A_B[j]+=int(S[i])
            if A_B[1]>A_B[0]:return 'TEAM-B '+str(i+1)
            
    return 'TIE'
while 1:
    try:
        data = raw_input().strip()+'0'
        if len(data) == 0:
            raise EOFError
        print penaltyShootOut(data)
    except:
        break
