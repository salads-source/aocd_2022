from aocd import get_data

input = get_data(day=1, year=2022)


def parse(puzzle_input):
    ref, ref_list = puzzle_input.split('\n\n'), []
    for i in ref:
        ref_list.append(i.split('\n'))
    return ref_list


def find_max(input):
    cal_max, inp = 0, parse(input)
    for i in inp:
        cov = list(map(int, i))
        if sum(cov) > cal_max:
            cal_max = sum(cov)
    return cal_max


def find_top_three(input):
    food_list, inp = [], parse(input)
    for i in inp:
        cov = list(map(int, i))
        food_list.append(sum(cov))
    sorted_food = sorted(food_list, reverse=True)
    return sum(sorted_food[:3])


print(find_max(input))
print(find_top_three(input))

