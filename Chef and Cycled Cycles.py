for _ in xrange(input()):
    N,Q = map(int,raw_input().strip().split())   
    cycles = [[0] for __ in xrange(N)]
    for i in xrange(N):
        temp = map(int,raw_input().strip().split())
        x = 0
        if N == 1 and temp[0] <=1:x = thy
        for j in xrange(temp[0]):
            x+= temp[j+1]
            cycles[i].append(x)
    bigCycle = [0]*(N+1)
    #each connector for the left and right connected cycles to a cycle
    # i.e  -left-^cycle^--right(left)-^cycle^--right-
    connectors = [[None,None] for __ in xrange(N)]
    x = 0
    for i in xrange(N):
        #right,left,weight
        temp = map(int,raw_input().strip().split())
        x+= temp[2]
        bigCycle[i+1]= x
        connectors[i][1] = temp[0]
        connectors[(i+1)%N][0] = temp[1]
    cyclePath = [0]*(N+1)
    path = 0
    #precompute minimum path transversing through a cycle
##    print 'connector paths','\n'
    for i in xrange(N):
        a,b = sorted(connectors[i])
        c = len(cycles[i])-1
        path += min(cycles[i][b-1]-cycles[i][a-1],cycles[i][c]-cycles[i][b-1]+cycles[i][a-1])
        cyclePath[i+1]= path
##        print i,': ',cycles[i][b-1]-cycles[i][a-1],cycles[i][c]-cycles[i][b-1]+cycles[i][a-1]
##    print ''
   #code starts here
    for __ in xrange(Q):
        v1,c1,v2,c2 = map(int,raw_input().strip().split())
        if c1>c2:
            v1,c1,v2,c2 = v2,c2,v1,c1
        if c1-c2 == 0:x = thy
        #left right values for each cycle
        cy1 = [0,0]
        cy2 = [0,0]
        _c1 = len(cycles[c1-1])-1
        _c2 = len(cycles[c2-1])-1
        #print 'v\'s :',v1,v2
        for i in xrange(2):
            a1 = connectors[c1-1][i]
            a2 = connectors[c2-1][i]
            b1,b2 = v1,v2
            #print 'a\'s :',a1,a2
            if a1>b1:
                a1,b1 = b1,a1
            if a2>b2:
                a2,b2 = b2,a2
            cy1[i] = min(cycles[c1-1][b1-1]-cycles[c1-1][a1-1],cycles[c1-1][_c1]-cycles[c1-1][b1-1]+cycles[c1-1][a1-1])
            cy2[i] = min(cycles[c2-1][b2-1]-cycles[c2-1][a2-1],cycles[c2-1][_c2]-cycles[c2-1][b2-1]+cycles[c2-1][a2-1])
            #print 'values :', a1,v1,_c1,' ',a2,v2,_c2
##            print i,':'
##            print cycles[c1-1][v1-1]-cycles[c1-1][a1-1],cycles[c1-1][_c1]-cycles[c1-1][v1-1]+cycles[c1-1][a1-1]
##            print cycles[c2-1][v2-1]-cycles[c2-1][a2-1],cycles[c2-1][_c2]-cycles[c2-1][v2-1]+cycles[c2-1][a2-1],'\n'
##        print 'cycle 1',cy1
##        print 'cycle 2',cy2,'\n'
            
        cy1_cy2 = (cyclePath[c2-1]-cyclePath[c1])+bigCycle[c2-1]-bigCycle[c1-1]
        
        cy2_cy1 = (cyclePath[N]-cyclePath[c2]+cyclePath[c1-1])+bigCycle[N]-bigCycle[c2-1]+bigCycle[c1-1]
##
##        print cy1_cy2
##        print cy2_cy1,'\n','Solution: ',
        print min(cy1[1]+cy1_cy2+cy2[0],cy2[1]+cy2_cy1+cy1[0])

#### Remove comment from below to see how data is stored                  
##    print 'cycles'
##    for i in xrange(N):print i+1,cycles[i]
##    print ''
##    print 'bigCycle'
##    print bigCycle,'\n'
##    print 'connectors'
##    print connectors,'\n'
##    print 'cyclePath'
##    print cyclePath
