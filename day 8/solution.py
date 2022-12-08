import sys
sys.path.append( '../' )

from utils import profiler
from functools import reduce

@profiler
def part1():
    print('Part 1')

    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    trees = []
    visibility = ''

    for line in lines:
        line = line.strip()
        trees.append(list(line))
    
    visibility = 'V' * len(trees)
    visibility += ('V' + '.' * (len(trees)-2) + 'V') * (len(trees)-2)
    visibility += 'V' * len(trees)

    while (visibility.find('.') > -1):
        current_tree = visibility.find('.')
        x = current_tree//len(trees)
        y = current_tree%len(trees)
        testing = ['V', 'V', 'V', 'V']
        for i in range(y):
            if trees[x][i] >= trees[x][y]:
                testing[0] = 'I'
                break
        for i in range(y+1, len(trees[x])):
            if trees[x][i] >= trees[x][y]:
                testing[1] = 'I'
                break
        for i in range(x):
            if trees[i][y] >= trees[x][y]:
                testing[2] = 'I'
                break
        for i in range(x+1, len(trees)):
            if trees[i][y] >= trees[x][y]:
                testing[3] = 'I'
                break
        if len(set(testing)) == 1 and testing[0] == 'I':
            visibility = visibility[:current_tree] + 'I' + visibility[current_tree+1:]
        else:
            visibility = visibility[:current_tree] + 'V' + visibility[current_tree+1:]

    print('Result:', visibility.count('V'))

@profiler
def part2():
    print('Part 2')

    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    trees = []
    visibility = ''

    for line in lines:
        line = line.strip()
        trees.append(list(line))
    
    visibility = 'V' * len(trees)
    visibility += ('V' + '.' * (len(trees)-2) + 'V') * (len(trees)-2)
    visibility += 'V' * len(trees)

    max = 0

    while (visibility.find('.') > -1):
        current_tree = visibility.find('.')
        x = current_tree//len(trees)
        y = current_tree%len(trees)
        testing = [0, 0, 0, 0]
        for i in range(y):
            if trees[x][i] >= trees[x][y]:
                testing[0] = 1
            else:
                testing[0] += 1
        for i in range(y+1, len(trees[x])):
            testing[1] += 1
            if trees[x][i] >= trees[x][y]:
                break               
        for i in range(x):
            if trees[i][y] >= trees[x][y]:
                testing[2] = 1
            else:
                testing[2] += 1
        for i in range(x+1, len(trees)):
            testing[3] += 1
            if trees[i][y] >= trees[x][y]:
                break
        score = reduce((lambda x, y: x * y), testing)
        if score > max:
            max = score
        visibility = visibility[:current_tree] + 'V' + visibility[current_tree+1:]

    print('Result:', max)

if __name__ == "__main__":
    part1()
    part2()