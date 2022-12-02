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

shape_losses = {
    "A": "B",
    "B": "C",
    "C": "A",
}

def score_round(theirs: str, outcome: str) -> int:
    if outcome == "Z":  # win
        return 6 + shape_scores[shape_losses[theirs]]
    if outcome == "Y":  # draw
        return 3 + shape_scores[theirs]
    if outcome == "X":  # lose
        return shape_scores[shape_wins[theirs]]


if __name__ == '__main__':
    with open('input.txt') as input:
        score = 0
        for line in input:
            score += score_round(line[0], line[2])

        print(score)
