from aocd import get_data
import re

input = get_data(day=5, year=2022)


def parse(puzzle_input):
    crate, com = puzzle_input.split('\n\n')
    com = [[int(d) for d in re.findall('\d+', line)] for line in com.strip().split('\n')]
    crate = crate.split('\n')
    return com, crate


def part_1(input):
    com, crate = parse(input)
    mat = []
    for i in range(1, 35, 4):
        stack = [c[i] for c in crate[:-1] if c[i] != ' ']
        mat.append(stack[::-1])
    for i in com:
        for j in range(0, i[0]):
            rem = mat[i[1] - 1].pop()
            mat[i[2] - 1].append(rem)
    return ''.join([i.pop() for i in mat])


def part_2(input):
    com, crate = parse(input)
    mat = []
    for i in range(1, 35, 4):
        stack = [c[i] for c in crate[:-1] if c[i] != ' ']
        mat.append(stack[::-1])
    for num, old, new in com:
        cut = len(mat[old - 1]) - num
        mat[new - 1] += mat[old - 1][cut:]
        mat[old - 1] = mat[old - 1][:cut]
    return ''.join([i.pop() for i in mat if i])












# print(final_state(input))
print(final_state2(input))



# print(parse(input))