from aocd import get_data

input = get_data(day=2, year=2022)


def parse(puzzle_input):
    ref = puzzle_input.split('\n')
    return ref


def find_total(input):
    ref_dict = {'X': 1, 'Y': 2, 'Z': 3}
    opp_dict = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    total, inp = 0, parse(input)
    for i in inp:
        if opp_dict[i[0]] == i[2]:
            total += 3 + ref_dict[i[2]]
        elif (i[0] == 'A' and i[2] == 'Z') or (i[0] == 'B' and i[2] == 'X') or (i[0] == 'C' and i[2] == 'Y'):
            total += 0 + ref_dict[i[2]]
        elif (i[0] == 'A' and i[2] == 'Y') or (i[0] == 'B' and i[2] == 'Z') or (i[0] == 'C' and i[2] == 'X'):
            total += 6 + ref_dict[i[2]]
    return total


def find_total2(input):
    ref_dict = {'X': 0, 'Y': 3, 'Z': 6}
    total, inp = 0, parse(input)
    for i in inp:
        if i[2] == 'X':
            if i[0] == 'A':
                total += 3
            elif i[0] == 'B':
                total += 1
            else:
                total += 2
        elif i[2] == 'Y':
            if i[0] == 'A':
                total += 1 + ref_dict[i[2]]
            elif i[0] == 'B':
                total += 2 + ref_dict[i[2]]
            else:
                total += 3 + ref_dict[i[2]]
        elif i[2] == 'Z':
            if i[0] == 'A':
                total += 2 + ref_dict[i[2]]
            elif i[0] == 'B':
                total += 3 + ref_dict[i[2]]
            else:
                total += 1 + ref_dict[i[2]]
    return total




print(find_total(input))
print(find_total2(input))

