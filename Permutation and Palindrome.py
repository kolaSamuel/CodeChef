from collections import defaultdict
for _ in xrange(input()):
    s = raw_input().strip()
    count = defaultdict(list)
    length = len(s)
    is_odd = length & 1
    is_palindrome = True

    for i in xrange(length):
        count[s[i]].append(i+1)

    for x in count:
        if len(count[x]) & 1:
            if is_odd: is_odd = False
            else: is_palindrome = False

    if is_palindrome:
        i, j = 0, -1
        result = [0]*length
        for x in count:
            y = len(count[x])
            if y & 1:
                y -= 1
                result[length/2] = count[x][-1]
            y /= 2
            for k in xrange(y):
                index = k*2
                result[i] = count[x][index]
                result[j] = count[x][index+1]
                i += 1
                j -= 1

        print " ".join(map(str, result))
    else:
        print -1
