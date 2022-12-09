from aocd import get_data

input = get_data(day=8, year=2022)


def parse(puzzle_input):
    ref, grid = puzzle_input.splitlines(), []
    for line in ref:
        row = [int(i) for i in line]
        grid.append(row)
    return grid


def part_1(input):
    count, inp = 0, parse(input)
    col, row = len(inp[0]), len(inp)

    for i in range(0, row):
        for j in range(0, col):
            curr = inp[i][j]

            top_col, bot_col = [inp[k][j] for k in range(0, i)], [inp[k][j] for k in range(i + 1, row)]
            left_row, right_row = [inp[i][d] for d in range(0, j)], [inp[i][d] for d in range(j + 1, col)]

            if all([i < curr for i in top_col]) or all([i < curr for i in bot_col]):
                count += 1
                continue
            if all([i < curr for i in left_row]) or all([i < curr for i in right_row]):
                count += 1
                continue

    return count


def part_2(input):
    score, inp = 0, parse(input)
    col, row = len(inp[0]), len(inp)

    for i in range(0, row):
        for j in range(0, col):
            curr = inp[i][j]

            top_col, bot_col = [inp[k][j] for k in range(0, i)], [inp[k][j] for k in range(i + 1, row)]
            left_row, right_row = [inp[i][d] for d in range(0, j)], [inp[i][d] for d in range(j + 1, col)]

            top_col.reverse()
            left_row.reverse()

            tc, bc, lr, rr = 0, 0, 0, 0

            for tree in top_col:
                if tree < curr:
                    tc += 1
                elif tree == curr:
                    tc += 1
                    break
                else:
                    break

            for tree in bot_col:
                if tree < curr:
                    bc += 1
                elif tree == curr:
                    bc += 1
                    break
                else:
                    break

            for tree in left_row:
                if tree < curr:
                    lr += 1
                elif tree == curr:
                    lr += 1
                    break
                else:
                    break

            for tree in right_row:
                if tree < curr:
                    rr += 1
                elif tree == curr:
                    rr += 1
                    break
                else:
                    break

            curr_score = tc * bc * lr * rr
            score = max(score, curr_score)

    return score


# print(part_2(input))