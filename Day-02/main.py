# Day 2 - Advent of Code 2022
# Parse Rock-Paper-Scisors tournament strategy guide and calulate
#  total predicted score based on either static moves (Part 1) or
#  based on the desired outcome(win/lose/tie) of the round (Part 2)


from typing import Union


def dynamic_decode_moves(moves:list) -> list:
    '''Decode moves according to strat guide, instuctions are win/lose/tie'''

    optimal_moves = []
    
    strat_key = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scisors',
        'X': 'lose',
        'Y': 'tie',
        'Z': 'win',
    }

    for move in moves:
        p1 = strat_key[move[0]]
        p2 = None
        if strat_key[move[1]] == 'tie':
            p2 = p1
            
        elif strat_key[move[1]] == 'win':
            if p1 == 'rock':
                p2 = 'paper'
            elif p1 == 'scisors':
                p2 = 'rock'
            else:
                p2 = 'scisors'

        # Throw the game
        else:
            if p1 == 'rock':
                p2 = 'scisors'
            elif p1 == 'scisors':
                p2 = 'paper'
            else:
                p2 = 'rock'

        optimal_moves.append([p1, p2])

    return optimal_moves

    
def static_decode_moves(moves:list) -> list:
    '''Decode moves according strat guide, instructions are which move'''
    
    strat_key = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scisors',
        'X': 'rock',
        'Y': 'paper',
        'Z': 'scisors',
    }

    return [ [ strat_key[move[0]], strat_key[move[1]] ] for move in moves ]


def read_guide(f_name:str, static:bool = True) -> list:
    '''Read predicted moves and sugested moves.  Sugestions are based on either a given move(static=True) or desired outcome(static=False)'''

    moves = []
    
    with open(f_name) as f:
        for line in f.readlines():
            moves.append(line.strip().split())

    if static:
        return static_decode_moves(moves)
        
    return dynamic_decode_moves(moves)

    
def score_game(choice1:str, choice2:str) -> Union[int, bool]:
    '''Score game based on chosen move and round outcome'''

    choices = {'rock': 1,
               'paper': 2,
               'scisors': 3,
               }

    if choice1 in choices.keys() and choice2 in choices.keys():
        score = choices[choice2.lower()]
    else:
        return False

    win = 6
    tie = 3
    lose = 0
    
    if choice1.lower() == 'rock':
        if choice2.lower() == 'rock':
            score += tie
        elif choice2.lower() == 'paper':
            score += win
        else:
            score += lose
    
    elif choice1.lower() == 'paper':
        if choice2.lower() == 'rock':
            score += lose
        elif choice2.lower() == 'paper':
            score += tie
        else:
            score += win
    
    elif choice1.lower() == 'scisors':
        if choice2.lower() == 'rock':
            score += win
        elif choice2.lower() == 'paper':
            score += lose
        else:
            score += tie

    return score


if __name__ == '__main__':


    game_scores = []

    my_moves = read_guide('strategy.txt', False)
    
    for game in my_moves:
        game_scores.append(score_game(*game))

    print(f'Predicted score of all games: {sum(game_scores)}')