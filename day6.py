from aocd import get_data

input = get_data(day=6, year=2022)


def parse(puzzle_input):
    ref = puzzle_input
    return list(ref)


def find_marker(input):
    pos, inp = 0, parse(input)
    while True:
        window = inp[pos: pos + 14]
        if len(window) == len(set(window)):
            break
        else:
            pos += 1
    return pos + 14

print(parse(input))
print(find_marker(input))
