lim = 31  # 2**31
n, q = map(int, raw_input().split())
arr = map(int, raw_input().split())

bits = [[0]*(n+1) for _ in xrange(lim)]


def initialize():
    for i in xrange(n):
        x = arr[i]
        for j in xrange(lim):
            mask = 1 << j
            bits[j][i] += bits[j][i-1]
            if mask & x:
                bits[j][i] += 1


initialize()

for _ in xrange(q):
    l, r = map(lambda x: int(x)-1, raw_input().split())

    ans = 0
    nums = r-l+1
    for i in xrange(lim):
        count = bits[i][r] - bits[i][l-1]
        if count < (nums+1)//2:
            ans += 1 << i

    print ans
