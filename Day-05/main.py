# Day 5 - Advent of Code 2022
# Elves are using a crane to arrange crates for ofload.  Predict
#  the order of crates so that the elves are ready for efficent
#  offload.  Find the order if the crane can only move one crate
#  at a time (Part 2).  Find the order if the crane can move
#  multiple crates at a time(Part 2).


def inital_state(f_name:str) -> list:
    '''read inital state from file.'''

    stacks = [list() for _ in range(10)]
    
    with open(f_name) as f:
        
        for line in f.readlines():
            if not '[' in line:
                break
                
            i = 1
            c = 1
            
            while i < len(line.strip()) and c < len(stacks):
                #print(line.strip())
                if line[i] != ' ':
                    stacks[c].append(line[i])
                i += 4
                c += 1

        for stack in stacks:
            stack.reverse()

    return stacks


def read_moves(f_name:str) -> list:
    '''Read moves from file. Return list of dicts with moves'''

    moves = []

    with open(f_name) as f:
        for line in f.readlines():
            if 'move' in line:
                parts = line.strip().split()
                move = {
                    'qty': int(parts[1]),
                    'src': int(parts[3]),
                    'dest': int(parts[5]),
                }
                moves.append(move)
            else:
                continue

    return moves


def part1(crates:list, moves:list):
    '''Move crates one at a time'''
    # Single crate per move (Part 1)
    for move in moves:
        for _ in range(move['qty']):
            crates[move['dest']].append(crates[move['src']].pop())

    print('Top most crates:')
    print(''.join([crate[-1] for crate in crates[1:]]))


def part2(crates:list, moves:list):
    '''Move multiple crates at a time'''

    for move in moves:
        for i in range(move['qty'],0,-1):
            crates[move['dest']].append(crates[move['src']].pop(-i))

    print('Top most crates:')
    print(''.join([crate[-1] for crate in crates[1:]]))


if __name__ == '__main__':

    in_file = 'input.txt'
    
    crates = inital_state(in_file)
    moves = read_moves(in_file)

    part1(crates, moves)
    
    crates = inital_state(in_file)
    part2(crates, moves)