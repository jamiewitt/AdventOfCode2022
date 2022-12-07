import sys
sys.path.append( '../' )

from utils import profiler
from collections import defaultdict

@profiler
def part1():
    print('Part 1')

    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    result = 0
    path = []
    dir_sizes={"/": 0}

    for line in lines:
        line = line.strip()
        if line.startswith('$ ls'):
            continue
        if line.startswith('$ cd'):
            new_dir = line.split()[-1]
            if new_dir == '/':
                path.clear()
                path.append('/')
            elif new_dir == '..':
                path.pop()
            else:
                path.append(new_dir)
        elif line.startswith('dir'):
            full_path = "/".join([str(item) for item in path])[1:] + "/" + line.split()[1]
            dir_sizes[full_path] = 0 
        else:
            file_size = int(line.split()[0])
            for segment in range(len(path)):
                full_path = "/".join([str(item) for item in path[:segment+1]])
                if len(full_path) > 1:
                    full_path = full_path[1:]
                dir_sizes[full_path] += file_size

    totals = sorted(dir_sizes.values())
    for dir_size in totals:
        if (dir_size) > 100000:
            break
        result += dir_size
    print('Result:', result)

@profiler
def part2():
    print('Part 2')

    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    result = 0
    path = []
    dir_sizes={"/": 0}

    for line in lines:
        line = line.strip()
        if line.startswith('$ ls'):
            continue
        if line.startswith('$ cd'):
            new_dir = line.split()[-1]
            if new_dir == '/':
                path.clear()
                path.append('/')
            elif new_dir == '..':
                path.pop()
            else:
                path.append(new_dir)
        elif line.startswith('dir'):
            full_path = "/".join([str(item) for item in path])[1:] + "/" + line.split()[1]
            dir_sizes[full_path] = 0 
        else:
            file_size = int(line.split()[0])
            for segment in range(len(path)):
                full_path = "/".join([str(item) for item in path[:segment+1]])
                if len(full_path) > 1:
                    full_path = full_path[1:]
                dir_sizes[full_path] += file_size

    space_free = 70000000 - dir_sizes['/']
    space_needed = 30000000 - space_free
    totals = sorted(dir_sizes.values())
    for dir_size in totals:
        if (dir_size) >= space_needed:
            result = dir_size
            break
    print('Result:', result)

if __name__ == "__main__":
    part1()
    part2()