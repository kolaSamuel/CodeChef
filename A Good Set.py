t =  input()
for i in xrange(t):
    gsl = input()
    ans = [1];c = 2
    while len(ans) < gsl:
        if not(any(c-x in ans for x in ans)):ans.append(c)
        c+=1         
    print " ".join(str(x) for x in ans)
#NAS#
##The answer is simlpy a list of odd numbers,because the sum of
##any two odd numbers would give an even, so a list of just odd numbers
##would solve the problem
