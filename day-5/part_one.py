from typing import Iterable, List

Map = List[List[str]]

def consume_map(lines: Iterable[str]) -> Map:
    stacks = []

    for line in lines:
        if line.startswith(" 1 "):  # Map key marker
            return [list(reversed(stack)) for stack in stacks]

        # Ensure we have enough stacks in our map
        while len(stacks) < (len(line) + 1) // 4:
            stacks.append([])

        for stack in range(0, len(line), 4):
            crate = line[stack + 1:stack + 2]
            if crate != ' ':
                stacks[stack // 4].append(crate)

    raise Exception()

def move_crate(map: Map, from_: int, to: int):
    crate = map[from_].pop()
    map[to].append(crate)

if __name__ == '__main__':
    with open('input.txt') as input:
        map = consume_map(input)

        next(input)  # Consume blank line

        print(map)

        for instruction in input:
            # move X from Y to Z
            words = instruction.split(" ")
            count = int(words[1])
            from_ = int(words[3]) - 1
            to = int(words[-1]) - 1

            for _ in range(0, count):
                move_crate(map, from_, to)

            print(instruction, map)

        print("".join(stack.pop() for stack in map))