import sys
sys.path.append( '../' )

from utils import profiler
from collections import defaultdict

@profiler
def part1():
    print('Part 1')

    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    visited = [[0,0]]
    h_location = [0, 0]
    t_location = [0, 0]

    for line in lines:
        line = line.strip()
        (direction, steps) = line.split()
        steps = int(steps)
        for i in range(steps):
            if (direction == 'R'):
                h_location[0] += 1
            elif (direction == 'L'):
                h_location[0] -= 1
            elif (direction == 'U'):
                h_location[1] += 1
            elif (direction == 'D'):
                h_location[1] -= 1
            
            distance = abs(h_location[0] - t_location[0]) + abs(h_location[1] - t_location[1])
            if distance == 3:
                if (direction == 'R'):
                    t_location[0] += 1
                    t_location[1] = h_location[1]
                elif (direction == 'L'):
                    t_location[0] -= 1
                    t_location[1] = h_location[1]
                elif (direction == 'U'):
                    t_location[0] = h_location[0]
                    t_location[1] += 1
                elif (direction == 'D'):
                    t_location[0] = h_location[0]
                    t_location[1] -= 1
            elif abs(h_location[0] - t_location[0]) > 1:
                if (direction == 'R'):
                    t_location[0] += 1
                elif (direction == 'L'):
                    t_location[0] -= 1
                elif (direction == 'U'):
                    t_location[0] += 1
                elif (direction == 'D'):
                    t_location[0] -= 1
            elif abs(h_location[1] - t_location[1]) > 1:
                if (direction == 'R'):
                    t_location[1] += 1
                elif (direction == 'L'):
                    t_location[1] -= 1
                elif (direction == 'U'):
                    t_location[1] += 1
                elif (direction == 'D'):
                    t_location[1] -= 1
            if (t_location not in visited):
                visited.append([t_location[0], t_location[1]])
                
    print(f'Visited: {len((visited))}')


@profiler
def part2():
    print('Part 2')

    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    visited = [[0,0]]
    locations = [[0, 0], [0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0]]

    for line in lines:
        line = line.strip()
        (direction, steps) = line.split()
        steps = int(steps)

        for i in range(steps):
            if (direction == 'R'):
                locations[0][0] += 1
            elif (direction == 'L'):
                locations[0][0] -= 1
            elif (direction == 'U'):
                locations[0][1] += 1
            elif (direction == 'D'):
                locations[0][1] -= 1
            for i in range(len(locations)-1):
                h_location = locations[i]
                t_location = locations[i+1]
                
                distance = abs(h_location[0] - t_location[0]) + abs(h_location[1] - t_location[1])
                if distance >= 3:
                    t_location[0] += 1 if h_location[0] > t_location[0] else -1
                    t_location[1] += 1 if h_location[1] > t_location[1] else -1
                elif abs(h_location[0] - t_location[0]) > 1:
                    t_location[0] += 1 if h_location[0] > t_location[0] else -1
                elif abs(h_location[1] - t_location[1]) > 1:
                    t_location[1] += 1 if h_location[1] > t_location[1] else -1
            if (locations[-1] not in visited):
                visited.append([locations[-1][0], locations[-1][1]])

    print(f'Visited: {len((visited))}')

if __name__ == "__main__":
    part1()
    part2()