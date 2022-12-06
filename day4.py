from aocd import get_data

input = get_data(day=4, year=2022)


def parse(puzzle_input):
    ref = puzzle_input.split('\n')
    return ref


def part_1(input):
    total, inp = 0, parse(input)
    for i in inp:
        task = i.split(',')
        t1, t2, t1_rng, t2_rng = task[0].split('-'), task[1].split('-'), [], []
        t1_rng = [i for i in range(int(t1[0]), int(t1[1]) + 1)]
        t2_rng = [i for i in range(int(t2[0]), int(t2[1]) + 1)]
        if set(t1_rng).issubset(set(t2_rng)) or set(t2_rng).issubset(set(t1_rng)):
            total += 1
    return total


def part_2(input):
    total, inp = 0, parse(input)
    for i in inp:
        task = i.split(',')
        rng_list = [list(map(int, task[0].split('-'))), list(map(int, task[1].split('-')))]
        rng_list.sort(key=lambda x: x[0])
        for j in range(1, len(rng_list)):
            if rng_list[j - 1][1] >= rng_list[j][0]:
                total += 1
    return total


# print(part_1(input))
# print(part_2(input))