from aocd import get_data
import string

input = get_data(day=3, year=2022)


def parse(puzzle_input):
    ref = puzzle_input.split('\n')
    return ref


def find_total(input):
    total, inp = 0, parse(input)
    for i in inp:
        mid = len(i) // 2
        L = i[:mid]
        R = i[mid:]
        for v, c in enumerate(string.ascii_letters):
            if c in L and c in R:
                total += v + 1
    return total


def find_total2(inout):
    total, inp = 0, parse(input)
    for i in range(0, len(inp), 3):
        grp = [inp[i], inp[i + 1], inp[i + 2]]
        for v, c in enumerate(string.ascii_letters):
            if c in grp[0] and c in grp[1] and c in grp[2]:
                total += v + 1
    return total





print(find_total(input))
print(find_total2(input))
# print(parse(input))