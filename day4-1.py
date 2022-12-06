def get_sections_set(section: str) -> set:
    """ Example input : '3-6' 
    Example output : (3,4,5,6) """

    # nice one liner right ? although a bit wasteful since we split twice.
    return set(range(int(section.split("-")[0]), int(section.split("-")[1]) + 1))


if __name__ == "__main__":
    with open("inputs/day4-1.txt") as file:
        pairs = [pair.split(",") for pair in file.read().splitlines()]
        # convert pairs to sections
        pairs = [(get_sections_set(pair[0]), get_sections_set(pair[1]))
                 for pair in pairs]

        fully_contained = 0

        for pair in pairs:
            # if the first set is fully contained in the second set
            if pair[0].issubset(pair[1]):
                fully_contained += 1
            # and vice versa
            elif pair[1].issubset(pair[0]):
                fully_contained += 1

        with open("outputs/day4-1.txt", "w") as file:
            file.write(str(fully_contained))
