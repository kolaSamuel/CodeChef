from bisect import bisect_left, bisect_right

for _ in xrange(input()):
    n = input()
    arr = map(int, raw_input().split())
    for i in xrange(1, n):
        arr[i] += arr[i - 1]

    result = [0] * (n+1)
    # print arr
    for i in xrange(n):
        x = arr[i] - arr[i - 1] if i > 0 else arr[i]

        left = bisect_left(arr, arr[i] - 2*x)
        right = min(bisect_right(arr, arr[i] + x)+1, n)

        result[left] += 1
        result[i] -= 1
        result[i+1] += 1
        result[right] -= 1

        # print i, left, right, x
        # print result
        # print

    # print result
    for i in xrange(1, n):
        result[i] += result[i - 1]
    print " ".join(str(result[x]) for x in xrange(n))


