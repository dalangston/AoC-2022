# Day 3 - Advent of Code 2022
# Elf rucksacks (packs) are mis-packed.  Find the item that is packed
#  in both compartments of the pack, and sum the value for all elves
#  (part 1), then find which item is the elf group id badge (badge),
#  it is the only item common among each 3 elf group (part 2)


def read_input(f_name:str) -> list:
    '''Read list of pack contents; return list of strings
    representing each elf's pack contents'''

    with open(f_name) as f:
        return [line.strip() for line in f.readlines()]


def get_compartments(pack_list:str) -> set:
    '''Split <pack_list> into two sets; return list contiaing
    one set for earch compartment'''

    mid = len(pack_list)//2

    compartment1 = set(pack_list[:mid])
    compartment2 = set(pack_list[mid:])

    return [compartment1, compartment2]


def item_priority(item:str) -> int:
    '''returns priority score of <item>'''

    items = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    return items.index(item) + 1


def part1():
    '''Score and sum items that appear in both pack compartments'''

    elf_packs = [get_compartments(pack) for pack in read_input('input')]
    mis_packs = [(pack[0] & pack[1]).pop() for pack in elf_packs]
    
    print(sum([item_priority(item) for item in mis_packs]))
    

def part2():
    '''Score and sum group badges'''

    elf_packs = [set(pack) for pack in read_input('input')]
    badges = []

    idx = 0

    while idx < len(elf_packs):
        badge = elf_packs[idx] & elf_packs[idx + 1] & elf_packs[idx + 2]
        badges.append(badge.pop())
        idx += 3

    print(sum([item_priority(item) for item in badges]))
    

if __name__ == '__main__':
    
    print('The sum of all items found mis-packed:')
    part1()
    print()

    print('The sum of all items that are group badges')
    part2()
    