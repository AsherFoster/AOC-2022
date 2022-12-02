def yield_elfs(fd):
    elf_sum = 0
    for line in fd:
        if line == '\n':
            yield elf_sum
            elf_sum = 0
        else:
            elf_sum += int(line)


if __name__ == '__main__':
    with open('input.txt') as input:
        elfs = sorted(list(yield_elfs(input)), reverse=True)

        print(sum(elfs[:3]))

