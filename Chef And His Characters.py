from itertools import permutations


def magic(x):
    result = 0
    for y in x:
        result *= 26
        result += ord(y)-96
    return result


mix = [magic(x) for x in permutations('chef')]

for _ in xrange(input()):
    string = raw_input().strip()
    size = len(string)
    count = 0
    if size > 3:
        for i in xrange(size-3):
            temp = string[i:i+4]
            if temp in mix: count += 1
    print ('lovely ' + str(count)) if count else 'normal'
