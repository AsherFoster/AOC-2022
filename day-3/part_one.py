if __name__ == '__main__':
    with open('input.txt') as input:
        total = 0
        for line in input:
            # 4 items, [:2], [2:]
            line = line[:-1]  # trim \n
            compartment_a = set(line[:int(len(line) / 2)])
            compartment_b = set(line[int(len(line) / 2):])

            error = compartment_a.intersection(compartment_b).pop()

            score = ord(error) - 96
            if score < 0:
                score += 58

            total += score

        print(total)
