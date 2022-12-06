from typing import List


def get_score_from_shape(shape: str) -> int:
    if shape == "X":  # X : Rock
        return 1
    elif shape == "Y":  # Y : Paper
        return 2
    elif shape == "Z":   # Z : Scissors
        return 3
    else:
        raise Exception("Invalid shape")


def get_score_from_move(opponent_shape: str, player_shape: str) -> int:
    """
    If win get 6 points
    If draw get 3 points
    If lose get 0 points
    """
    if opponent_shape == "A":  # X : Rock
        if player_shape == "X":  # X : Rock
            return 3
        elif player_shape == "Y":  # Y : Paper
            return 6
        elif player_shape == "Z":  # Z : Scissors
            return 0
        else:
            raise Exception(
                f"Invalid move {player_shape} against {opponent_shape}")
    elif opponent_shape == "B":  # Y : Paper
        if player_shape == "X":  # X : Rock
            return 0
        elif player_shape == "Y":  # Y : Paper
            return 3
        elif player_shape == "Z":  # Z : Scissors
            return 6
        else:
            raise Exception(
                f"Invalid move {player_shape} against {opponent_shape}")
    elif opponent_shape == "C":  # Z : Scissors
        if player_shape == "X":  # X : Rock
            return 6
        elif player_shape == "Y":  # Y : Paper
            return 0
        elif player_shape == "Z":  # Z : Scissors
            return 3
        else:
            raise Exception(
                f"Invalid move {player_shape} against {opponent_shape}")
    else:
        raise Exception(
            f"Invalid move {player_shape} against {opponent_shape}")


def get_score_from_round(round: List[str]) -> int:
    first_part = get_score_from_shape(round[1])
    second_part = get_score_from_move(round[0], round[1])

    return first_part + second_part


if __name__ == "__main__":

    total = 0

    with open("inputs/day2-1.txt") as file:
        rounds = [current_round.split(" ")
                  for current_round in file.read().splitlines()]

        for current_round in rounds:
            total += get_score_from_round(current_round)

    with open("outputs/day2-1.txt", "w") as file:
        file.write(str(total))
