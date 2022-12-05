if __name__ == "__main__":
    elvesCalories = []
    with open("inputs/day1-1.txt") as f:
        data = f.read().splitlines()
        current = 0
        for index, input in enumerate(data):
            if input == "" or index == len(data) - 1:
                elvesCalories.append(current)
                current = 0
            else:
                current += int(input)

    elvesCalories.sort(reverse=True)
    with open("outputs/day1-1.txt", "w") as f:
        f.write(str(elvesCalories[0]))
