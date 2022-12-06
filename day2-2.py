from typing import List


def get_score_from_shape(shape: str) -> int:
    if shape == "rock":
        return 1
    elif shape == "paper":
        return 2
    elif shape == "scissors":
        return 3
    else:
        raise Exception("Invalid shape")


def get_score_from_move(strategy: str) -> int:
    if strategy == "X":  # I need to lose
        return 0
    elif strategy == "Y":  # I need to draw
        return 3
    elif strategy == "Z":  # I need to win
        return 6
    else:
        raise Exception(f"Invalid strategy {strategy}")


def get_corresponding_shape(opponent_shape: str, strategy: str) -> str:
    if opponent_shape == "A":  # A : Rock
        if strategy == "X":  # I need to lose
            return "scissors"
        elif strategy == "Y":  # I need to draw
            return "rock"
        elif strategy == "Z":  # I need to win
            return "paper"
        else:
            raise Exception(f"Invalid strategy {strategy}")

    elif opponent_shape == "B":  # B : Paper
        if strategy == "X":  # I need to lose
            return "rock"
        elif strategy == "Y":  # I need to draw
            return "paper"
        elif strategy == "Z":  # I need to win
            return "scissors"
        else:
            raise Exception(f"Invalid strategy {strategy}")
    elif opponent_shape == "C":  # C : Scissors
        if strategy == "X":  # I need to lose
            return "paper"
        elif strategy == "Y":  # I need to draw
            return "scissors"
        elif strategy == "Z":  # I need to win
            return "rock"
        else:
            raise Exception(f"Invalid strategy {strategy}")
    else:
        raise Exception(f"Invalid move {opponent_shape} - {strategy}")


if __name__ == "__main__":

    total = 0

    with open("inputs/day2-1.txt") as file:
        rounds = [current_round.split(" ")
                  for current_round in file.read().splitlines()]

        for current_round in rounds:
            shape = get_corresponding_shape(current_round[0], current_round[1])
            shape_score = get_score_from_shape(shape)
            move_score = get_score_from_move(current_round[1])
            total += shape_score + move_score

    with open("outputs/day2-2.txt", "w") as file:
        file.write(str(total))
