from typing import Tuple, Set


def create_range_set(elf: str) -> Set[int]:
    start, end = (int(x) for x in elf.split("-"))

    return set(range(start, end + 1))


if __name__ == "__main__":
    with open("input.txt") as input:
        includes = 0
        overlapping = 0

        for line in input:
            elf_a, elf_b = (create_range_set(elf) for elf in line.split(","))  # type: Set[int], Set[int]  # (screaming internally)

            if elf_a.issubset(elf_b) or elf_b.issubset(elf_a):
                includes += 1

            if elf_a & elf_b:
                overlapping += 1

        print("includes: ", includes)
        print("overlapping: ", overlapping)