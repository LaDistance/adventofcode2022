
def run_instruction(line: str, stacks: list[list[str]]) -> None:
    """ Run an instruction on the stacks
        Example instruction : 'move 2 from 8 to 2'
        This instruction means that we need to move the top 2 blocks from stack 8 to stack 2
    """
    # Split the instruction into its parts
    instruction = line.split(" ")
    # Get the number of blocks to move
    number_of_blocks = int(instruction[1])
    # Get the source stack
    source_stack = int(instruction[3])
    # Get the destination stack
    destination_stack = int(instruction[5])
    # Blocks to move
    blocks = stacks[source_stack - 1][:number_of_blocks]
    # Remove the blocks from the source stack
    stacks[source_stack - 1] = stacks[source_stack - 1][number_of_blocks:]
    # Add the blocks to the destination stack
    stacks[destination_stack - 1] = [*blocks, *stacks[destination_stack - 1]]


if __name__ == "__main__":
    with open("inputs/day5-1.txt") as file:
        lines = file.read().splitlines()
        # First we need to read the first part of the file
        # It contains the 9 stacks

        # Initialize the stacks
        stacks = [[] for i in range(9)]
        # Loop through the lines
        for line in lines[:8]:
            for i in range(1, 36, 4):
                # if line[i] is in the alphabet
                if line[i].isalpha():
                    # Add the letter to the stack
                    stacks[i//4].append(line[i])

        # Run the instructions
        for line in lines[10:]:
            print(line)

            try:
                run_instruction(line, stacks)
            except IndexError:
                print(f"IndexError : {line}, stacks : {stacks}")

        # Get the top of each stack
        top_of_stacks = [stack[0] for stack in stacks]

        with open("outputs/day5-2.txt", "w") as file:
            file.write("".join(top_of_stacks))
