import sys
sys.path.append( '../' )

from utils import profiler

@profiler
def part1():
    file1 = open('input.txt', 'r')

    lines = file1.readlines()

    score_card = {
        'A': 1,
        'B': 2,
        'C': 3,
    }

    equivalent = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C',
    }

    wld = {
        'win': 6,
        'loss': 0,
        'draw': 3
    }

    score = 0

    for line in lines:
        (opponent, player) = line.strip().split()
        player = equivalent[player]
        if opponent == 'A' and player == 'C':
            score += wld['loss'] + score_card[player]
        elif opponent == 'C' and player == 'A':
            score += wld['win'] + score_card[player]
        elif player > opponent:
            score += wld['win'] + score_card[player]
        elif player == opponent:
            score += wld['draw'] + score_card[player]
        elif player < opponent:
            score += wld['loss'] + score_card[player]

    print(score)

@profiler
def part2():
    file1 = open('input.txt', 'r')

    lines = file1.readlines()

    score_card = {
        'A': 1,
        'B': 2,
        'C': 3,
    }

    wld = {
        'win': 6,
        'loss': 0,
        'draw': 3
    }

    rps = ['A', 'B', 'C']

    score = 0

    for line in lines:
        (opponent, result) = line.strip().split()
        if result == 'Z':
            player = rps[(ord(opponent)+1 - 65) % 3]
        elif result == 'Y':
            player = opponent
        else:
            player = rps[(ord(opponent)-1 - 65) % 3]

        if opponent == 'A' and player == 'C':
            score += wld['loss'] + score_card[player]
        elif opponent == 'C' and player == 'A':
            score += wld['win'] + score_card[player]
        elif player > opponent:
            score += wld['win'] + score_card[player]
        elif player == opponent:
            score += wld['draw'] + score_card[player]
        elif player < opponent:
            score += wld['loss'] + score_card[player]

    print(score)

if __name__ == "__main__":
    part1()
    part2()