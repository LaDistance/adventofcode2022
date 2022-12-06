if __name__ == "__main__":
    with open("inputs/day4-1.txt") as file:
        backpacks = file.read().splitlines()

        backpacks = [set(backpack) for backpack in backpacks]
        # group the backpacks in groups of 3
        groups = [backpacks[i:i+3] for i in range(0, len(backpacks), 3)]

        badges = [set.intersection(*group) for group in groups]

        total = 0
        for badge in badges:
            for character in badge:
                if(character.isupper()):
                    total += ord(character) - 38
                else:
                    total += ord(character) - 96
    with open("outputs/day3-2.txt", "w") as file:
        file.write(str(total))
