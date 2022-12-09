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
        self.cwd = self.root
        self.prev_dirs = []
        self.dir_size = {}

    def cd(self, cmd):
        if cmd == '..':
            prev = parent.root if len(self.prev_dirs) == 1 else self.prev_dirs[-1]
            self.prev_dirs.pop()
            self.cwd = prev
        else:
            self.prev_dirs.append(self.cwd)
            self.cwd = self.cwd.directories[cmd]
            name = [i.name for i in self.prev_dirs]
            name.append(self.cwd.name)
            self.dir_size['/'.join(name)] = 0

    def add_dir(self, dir):
        self.cwd.add_directory(dir)

    def add_file(self, name, size):
        self.cwd.add_file(name, size)
        name = [i.name for i in self.prev_dirs]
        name.append(self.cwd.name)
        if self.dir_size.get('/'.join(name), 0) == 0:
            self.dir_size['/'.join(name)] = int(size)
        else:
            self.dir_size['/'.join(name)] += int(size)
        for j in range(0, len(self.prev_dirs)):
            name_new = [k.name for k in self.prev_dirs]
            path = '/'.join(name_new[:j + 1])
            if path in self.dir_size:
                self.dir_size[path] += int(size)


inp, parent = parse(input), FileSystem()

for i in range(1, len(inp)):
    cmd = inp[i].split()

    if cmd[0] == '$':
        if cmd[1] == 'cd':
            if cmd[2] == '..':
                parent.cd(cmd[2])
            else:
                parent.cd(cmd[2])

        elif cmd[1] == 'ls':
            pass
    elif cmd[0] == 'dir':
        parent.add_dir(cmd[1])
    else:
        parent.add_file(cmd[1], cmd[0])

small_dirs = {k: v for (k, v) in parent.dir_size.items() if v <= 100000}
print(f"part_1: {sum(small_dirs.values())}")

size_req = 30000000 - (70000000 - parent.dir_size.get('/'))
dir_sort = sorted([(k, v) for (k, v) in parent.dir_size.items()], key=lambda x: x[1])

for path, size in dir_sort:
    if size >= size_req:
        print(f'part_2: {size}')
        break



