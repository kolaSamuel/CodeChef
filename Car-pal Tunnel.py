for _ in xrange(input()):
    N = input()
    A = map(int, raw_input().split())
    C, D, S = map(int, raw_input().split())

    _max = max(A)
    # if D/S > 1: x = 7/0
    print (C-1)*_max
