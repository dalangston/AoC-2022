# Day 1 - Advent of Code
# Parse list of calories carried by each elf and calculate the most
#  calories carried by one elf (Part 1) and the total amount of
#  calories carried by the 3 elves with them most calories


def elf_cal_list(f_name:str) -> list:
    '''Read <f_name>; return list of lists with each elf's calories'''

    cals_per_elf = []

    with open(f_name) as f:
        elf_cal = []
        for line in f.readlines():
            l = line.strip()
            if l == '':
                cals_per_elf.append(elf_cal)
                elf_cal = []
                continue
            elf_cal.append(int(l))

    return cals_per_elf



if __name__ == '__main__':

    # Part 1
    # Calories carried by the elf with the most calories
    f_name = 'calories.txt'
    elf_calories = elf_cal_list(f_name)
    max_cals = max([sum(x) for x in elf_calories])

    print(f'Elf with the most calories is carrying {max_cals} calories')
    print()

    # Part 2
    # Calories carried by the 3 elves with the most caloreis
    top_3 = [sum(x) for x in elf_calories]
    top_3.sort(reverse=True)
    print(f'The top 3 elves are carrying {sum(top_3[:3])} calories')
