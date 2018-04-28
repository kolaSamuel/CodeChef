from collections import defaultdict
from bisect import bisect
from math import ceil


def new_k(val, x, k):
    if val > x:
        x, val = val, x
    if x - val > k:
        x = val + 1 + k
        k = 0
    else:
        k -= x - val - 1
    for i in xrange(int(val + 1), int(x)):
        print i, int(y)
    return k


for _ in xrange(input()):
    N = input()
    k = 10  # N // 10

    # creating lines
    start_x, start_y = map(float, raw_input().split())
    lines = []
    checks = defaultdict(list)
    checks[start_y].append(start_x)
    prev_x, prev_y = start_x, start_y

    for _ in xrange(N-1):
        x, y = map(float, raw_input().split())
        try:
            m = (y - prev_y)/(x - prev_x)
            c = y - m*x
            lines.append((max(y, prev_y), m, c, x, prev_x))
        except ZeroDivisionError:
            m = 'a'
            lines.append((max(y, prev_y), m, x, y, prev_y))

        if y in checks and y != prev_y and y != start_y:
            k = new_k(checks.pop(y)[0], x, k)
        else:
            checks[y].append(x)

        prev_x, prev_y = x, y
        if k == 0:
            break
    else:
        # print 'Double ends'
        try:
            m = (start_x - prev_x)/(start_y - prev_y)
            c = start_y - m*start_x
            lines.append((max(start_y, prev_y), m, c, start_x, prev_x))
        except ZeroDivisionError:
            m = 'a'
            lines.append((max(y, prev_y), m, x, y, prev_y))

        lines.sort()
        length = len(lines)
        for y in checks:
            x = checks[y][0]
            start = bisect(lines, (y,))
            for pos in xrange(start, length):
                _y, m, c, x1, x2 = lines[pos]
                try:
                    intersect = y if m == 'a' else (y - c)/m
                except ZeroDivisionError:
                    continue
                if x1 < intersect < x2 or x2 < intersect < x1:
                    _x = c if m == 'a' else int(ceil(intersect))
                    k = new_k(_x, x, k)
                    break
            if k == 0:
                break
        else:
            print 'No more', k


