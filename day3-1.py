if __name__ == "__main__":

    total = 0

    with open("inputs/day3-1.txt") as file:
        backpacks = file.read().splitlines()
        # Split each string into half length
        for backpack in backpacks:
            first_part = backpack[:len(backpack)//2]
            second_part = backpack[len(backpack)//2:]
            # get all the characters present in both parts
            common_characters = set(first_part).intersection(set(second_part))
            # For each common character, add its value to the total
            for character in common_characters:
                if(character.isupper()):
                    total += ord(character) - 38
                else:
                    total += ord(character) - 96

    with open("outputs/day3-1.txt", "w") as file:
        file.write(str(total))
