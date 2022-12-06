if __name__ == "__main__":
    # Initialize the list of all elves' total calories
    calories = []
    # Open the file
    with open("inputs/day1-1.txt") as f:
        # Read the file and split it into lines
        data = f.read().splitlines()
        # Initialize the current total calories
        current = 0
        # Loop through the lines
        for index, input in enumerate(data):
            # If the line is empty or we're at the end of the file
            if input == "" or index == len(data) - 1:
                # Add the current total calories to the list
                calories.append(current)
                # Reset the current total calories
                current = 0
            else:
                # Default case
                # Add the current line's calories to the current total calories
                current += int(input)

    # Sort the list of all elves' total calories in descending order
    calories.sort(reverse=True)
    with open("outputs/day1-1.txt", "w") as f:
        # Write the sum of the first elve's total calories to the output file
        f.write(str(calories[0]))
