from aocd import get_data

input = get_data(day=7, year=2022)


def parse(puzzle_input):
    ref = puzzle_input.splitlines()
    return ref


class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content


class Directory:
    def __init__(self, name, prev):
        self.name = name
        self.prev = prev
        self.files = []
        self.directories = {}

    def add_file(self, name, content):
        self.files.append(File(name, content))

    def add_directory(self, name):
        self.directories[name] = Directory(name, self.directories)


class FileSystem:
    def __init__(self):
        self.prev = None
        self.root = Directory('/', self.prev)


inp, parent = parse(input), FileSystem()
cwd, prev_dirs, dir_size = parent.root, [], {}

for i in range(1, len(inp)):
    cmd = inp[i].split()

    if cmd[0] == '$':
        if cmd[1] == 'cd':
            if cmd[2] == '..':
                prev = parent.root if len(prev_dirs) == 1 else prev_dirs[-1]
                prev_dirs.pop()
                cwd = prev
            else:
                prev_dirs.append(cwd)
                cwd = cwd.directories[cmd[2]]
                name = [i.name for i in prev_dirs]
                name.append(cwd.name)
                dir_size['/'.join(name)] = 0

        elif cmd[1] == 'ls':
            pass
    elif cmd[0] == 'dir':
        cwd.add_directory(cmd[1])
    else:
        cwd.add_file(cmd[1], cmd[0])
        name = [i.name for i in prev_dirs]
        name.append(cwd.name)
        if dir_size.get('/'.join(name), 0) == 0:
            dir_size['/'.join(name)] = int(cmd[0])
        else:
            dir_size['/'.join(name)] += int(cmd[0])
        for j in range(0, len(prev_dirs)):
            name_new = [k.name for k in prev_dirs]
            path = '/'.join(name_new[:j+1])
            if path in dir_size:
                dir_size[path] += int(cmd[0])

small_dirs = {k: v for (k, v) in dir_size.items() if v <= 100000}
print(f"part_1: {sum(small_dirs.values())}")

size_req = 30000000 - (70000000 - dir_size.get('/'))
dir_sort = sorted([(k, v) for (k, v) in dir_size.items()], key=lambda x: x[1])
for path, size in dir_sort:
    if size >= size_req:
        print(f'part_2: {size}')
        break



