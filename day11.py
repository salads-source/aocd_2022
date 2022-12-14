from aocd import get_data
import re
import operator

input = get_data(day=11, year=2022)

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.xor,
}

def parse(puzzle_input):
    monkey = puzzle_input.split('\n\n')
    monkey_new = [i.split('\n') for i in monkey]
    return monkey_new


def part_1(puzzle):
    inp = parse(puzzle)
    monkey_items = [[int(d) for d in re.findall('\d+', line[1])] for line in inp]
    monkey_turns = [0 for _ in range(8)]
    monkey_commands = [[] for _ in range(8)]
    modulo = 1

    for i in range(8):
        monkey_commands[i].append([d for d in re.findall(r'[\+\-\*\/]', inp[i][2])][0])
        res = [int(d) for d in re.findall(r'\d+', inp[i][2])]
        monkey_commands[i].append(res[0]) if len(res) >= 1 else monkey_commands[i].append('old')
        monkey_commands[i].append([int(d) for d in re.findall(r'\d+', inp[i][3])][0])
        monkey_commands[i].append([int(d) for d in re.findall(r'\d+', inp[i][4])][0])
        monkey_commands[i].append([int(d) for d in re.findall(r'\d+', inp[i][5])][0])
        modulo *= [int(d) for d in re.findall(r'\d+', inp[i][3])][0]

    for _ in range(10000):
        for i in range(8):
            if len(monkey_items[i]) == 0:
                continue
            else:
                for j in monkey_items[i]:
                    curr_item = j
                    if monkey_commands[i][1] == 'old':
                        curr_item = pow(curr_item, 2)
                    else:
                        curr_item = ops[monkey_commands[i][0]](curr_item, monkey_commands[i][1])
                    # curr_item //= 3
                    curr_item %= modulo
                    if curr_item % monkey_commands[i][2] == 0:
                        monkey_items[monkey_commands[i][3]].append(curr_item)
                    else:
                        monkey_items[monkey_commands[i][4]].append(curr_item)
                    monkey_turns[i] += 1
                monkey_items[i] = []
    monkey_turns.sort(reverse=True)
    return monkey_turns[0] * monkey_turns[1]


# print(parse(input))
# print(part_1(input))