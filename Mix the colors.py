for _ in xrange(input()):
    n = input()
    arr = map(int, raw_input().split())
    b = len(set(arr))
    print n-b
