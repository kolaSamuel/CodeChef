from collections import Counter
for _ in xrange(input()):
    N, M, X, K = map(int,raw_input().split())
    workers = Counter(raw_input().strip())
    even = workers['E']
    odd = workers['O']
    even_workers = M/2
    odd_workers = M-even_workers

    max_work = min(even_workers*X, even) + min(odd_workers*X, odd)

    print 'yes' if max_work >= N else 'no'
