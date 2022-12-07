dirs = {"name": [""]}

# filesystem = {
#     "dir": ["a"],
#     "a": 123
# }
filesystem = {"": []}

SEP = "/"


def size_dir(name: str) -> int:
    size = 0

    for entry in filesystem[name]:
        val = filesystem[entry]
        if type(val) == list:
            size += size_dir(entry)
        else:
            size += val

    return size

with open('input.txt') as input:
    cwd = []

    while line := next(input, None):
        args = line[:-1].split(" ")
        if args[0] == '$':
            if args[1] == 'cd':
                if args[2] == '..':
                    cwd.pop()
                elif args[2] == '/':
                    cwd = []
                else:
                    cwd += args[2].split(SEP)

            elif args[1] == 'ls':
                # we can probably ignore these - just consume any dir listings as they come up
                pass
        elif args[0] == 'dir':
            path = SEP.join(cwd + [args[1]])
            filesystem[SEP.join(cwd)].append(path)
            if path not in filesystem:
                filesystem[path] = []
        else:
            name = SEP.join(cwd + [args[1]])
            filesystem[SEP.join(cwd)].append(name)
            size = int(args[0])
            filesystem[name] = size

    sized_dirs = {
        entry: size_dir(entry)
        for entry in filesystem
        if type(filesystem[entry]) == list
    }

    print("part one", sum(size for entry, size in sized_dirs.items() if size <= 100_000))
    print("total", size_dir(""))

    max_fs_size = 70000000 - 30000000
    must_delete = size_dir("") - max_fs_size
    print("must free up ", must_delete)
    print("part two", next((dir, size) for dir, size in sorted(sized_dirs.items(), key=lambda dir: dir[1]) if size > must_delete))
