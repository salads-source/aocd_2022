from aocd import get_data

input = get_data(day=10, year=2022)


def parse(puzzle_input):
    ref = puzzle_input
    com_list = ref.splitlines()
    return com_list


def check_cycle(cycle, X, total):
    cycle_track = [20, 60, 100, 140, 180, 220]
    if cycle in cycle_track:
        total += cycle * X
    return total


def part_1(input):
    total, cycle, X, inp = 0, 0, 1, parse(input)
    for command in inp:
        com = command.split()
        if com[0] == 'noop':
            cycle += 1
            total = check_cycle(cycle, X, total)
        else:
            for _ in range(2):
                cycle += 1
                total = check_cycle(cycle, X, total)
            X += int(com[1])
    return total


def part_2(input):
    X, inp = 1, parse(input)
    screen, row, pixel_pos = [], [], 0
    for command in inp:
        com = command.split()
        if com[0] == 'noop':
            if pixel_pos == X or pixel_pos == X + 1 or pixel_pos == X - 1:
                row.append('#')
            else:
                row.append('.')
            pixel_pos += 1
            if len(row) == 40:
                screen.append(row)
                row, pixel_pos = [], 0
        else:
            for _ in range(2):
                if pixel_pos == X or pixel_pos == X + 1 or pixel_pos == X - 1:
                    row.append('#')
                else:
                    row.append('.')
                pixel_pos += 1
                if len(row) == 40:
                    screen.append(row)
                    row, pixel_pos = [], 0
            X += int(com[1])

    for i in screen:
        print(i)









print(part_1(input))
print(part_2(input))