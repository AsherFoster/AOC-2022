if __name__ == '__main__':
    with open('input.txt') as input:
        max = 0
        elf_sum = 0
        for line in input:
            if line == '\n':
                if elf_sum > max:
                    max = elf_sum
                elf_sum = 0
            else:
                elf_sum += int(line)

    print(max)
