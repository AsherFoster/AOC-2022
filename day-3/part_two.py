def score(item: str) -> int:
    score = ord(item) - 96
    if score < 0:
        score += 58

    return score

if __name__ == '__main__':
    with open('input.txt') as input:
        total = 0

        lines = input.readlines()
        for i in range(0, len(lines), 3):
            badge = set.intersection(*(set(bag[:-1]) for bag in lines[i:i+3])).pop()

            total += score(badge)

        print(total)
