# X: Rock: 1
# Y: Paper: 2
# Z: Scissors: 3
shape_map = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

shape_scores = {
    "A": 1,
    "B": 2,
    "C": 3,
}

shape_wins = {
    "A": "C",
    "B": "A",
    "C": "B",
}

def score_round(theirs: str, mine: str) -> int:
    shape_score = shape_scores[mine]

    if mine == theirs:
        return shape_score + 3
    if shape_wins[mine] == theirs:
        return shape_score + 6
    return shape_score


if __name__ == '__main__':
    with open('input.txt') as input:
        score = 0
        for line in input:
            score += score_round(line[0], shape_map[line[2]])

        print(score)
