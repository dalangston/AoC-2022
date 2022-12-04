# Day 4 - Advent of Code 2022
# Elves are assigned areas to clear out and paired up.  Find pairs
#  for which one assighed area in a sub set of the partner's (Part 1).
#  Find all pairs for which there is any overlaping area (Part 2).


def read_input(f_name:str) -> list:

    pairs = []

    with open(f_name) as f:
        for line in f.readlines():
            pairs.append([l.strip() for l in line.split(',')])

    return pairs


if __name__ == '__main__':

    pairs = read_input('input')

    # Part 1: Fully enclosed 
    enclosed = 0

    for pair in pairs:
        elf1_bounds = [int(b) for b in pair[0].split('-')]
        elf2_bounds = [int(b) for b in pair[1].split('-')]

        if elf1_bounds[0] <= elf2_bounds[0] and elf1_bounds[1] >= elf2_bounds[1]:
            enclosed += 1
        elif elf2_bounds[0] <= elf1_bounds[0] and elf2_bounds[1] >= elf1_bounds[1]:
            enclosed += 1

    print(f'Pairs with one fully enclosed range:  {enclosed}')

    # Part 2: Any overlap
    overlap = 0

    for pair in pairs:
        elf1_bounds = [int(b) for b in pair[0].split('-')]
        elf2_bounds = [int(b) for b in pair[1].split('-')]

        # Does one range start within the other?
        if elf1_bounds[0] <= elf2_bounds[0] <= elf1_bounds[1]:
            overlap += 1
        elif elf2_bounds[0] <= elf1_bounds[0] <= elf2_bounds[1]:
            overlap += 1
        # Does one range end within the other?
        elif elf1_bounds[0] <= elf2_bounds[1] <= elf1_bounds[1]:
            overlap += 1
        elif elf2_bounds[0] <= elf1_bounds[1] <= elf2_bounds[1]:
            overlap += 1

    print(f'Pairs with any overlap: {overlap}')
