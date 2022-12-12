from aocd import get_data

input = get_data(day=9, year=2022)


def parse(puzzle_input):
    ref = puzzle_input
    com_list = ref.splitlines()
    return com_list


def move_head(head, direc):
    x, y = head
    if direc == 'L':
        x -= 1
    elif direc == 'R':
        x += 1
    elif direc == 'U':
        y += 1
    elif direc == 'D':
        y -= 1

    head = x, y
    return head



def tail_prox(head, tail):
    x_diff, y_diff = abs(head[0] - tail[0]), abs(head[1] - tail[1])
    if x_diff == 1 and y_diff == 1:
        return True
    elif x_diff == 1 and y_diff == 0:
        return True
    elif x_diff == 0 and y_diff == 1:
        return True
    elif x_diff == 0 and y_diff == 0:
        return True
    elif x_diff >= 2 or y_diff >= 2:
        return False


def move_tail(head, tail):
    x, y = tail

    if tail_prox(head, tail) is False:
        if head[0] - tail[0] > 0:
            shift_x = 1
        elif head[0] - tail[0] == 0:
            shift_x = 0
        else:
            shift_x = - 1

        if head[1] - tail[1] > 0:
            shift_y = 1
        elif head[1] - tail[1] == 0:
            shift_y = 0
        else:
            shift_y = - 1

        x += shift_x
        y += shift_y
    else:
        pass

    tail = x, y
    return tail


inp = parse(input)
# visited, head, tail = [(0, 0)], (0, 0), (0, 0)
visited, seq = [(0, 0)], [(0, 0) for _ in range(10)]
for command in inp:
    com = command.split(' ')
    for _ in range(int(com[1])):
        seq[0] = move_head(seq[0], com[0])
        for i in range(1, len(seq)):
            seq[i] = move_tail(seq[i - 1], seq[i])
        visited.append(seq[9])

print(len(set(visited)))  # part 2













