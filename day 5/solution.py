import sys
sys.path.append( '../' )

from utils import profiler
from collections import defaultdict

@profiler
def part1():
    print('Part 1')

    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    result = ''
    stacks = defaultdict(list)
    process_stacks = True
    instructions = []

    for line in lines:
        line = line.rstrip()

        if len(line) == 0:
            process_stacks = False
            continue
        
        if process_stacks:
            current_stack = 1
            while len(line) > 0:
                if len(line) == 3:
                    crate = line
                    line = ''
                else:
                    crate = line[:3]
                    line = line[4:]
                
                if crate.startswith('['):
                    stacks[current_stack].append(crate[1])
                current_stack += 1
        else:
            instructions.append(line)

    for instruction in instructions:
        (m, count, f, stack_1, t, stack_2) = instruction.split()
        for op in range(int(count)):
            crate = stacks[int(stack_1)].pop(0)
            stacks[int(stack_2)][:0] = [crate]

    for stack in range(1, len(stacks)+1):
        result += stacks[stack][0]

    print(result)

@profiler
def part2():
    print('Part 2')

    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    result = ''
    stacks = defaultdict(list)
    process_stacks = True
    instructions = []

    for line in lines:
        line = line.rstrip()

        if len(line) == 0:
            process_stacks = False
            continue
        
        if process_stacks:
            current_stack = 1
            while len(line) > 0:
                if len(line) == 3:
                    crate = line
                    line = ''
                else:
                    crate = line[:3]
                    line = line[4:]
                
                if crate.startswith('['):
                    stacks[current_stack].append(crate[1])
                current_stack += 1
        else:
            instructions.append(line)

    for instruction in instructions:
        (m, count, f, stack_1, t, stack_2) = instruction.split()
        for op in range(int(count)):
            stacks[int(stack_2)][:0] = stacks[int(stack_1)][:int(count)]
            stacks[int(stack_1)] = stacks[int(stack_1)][int(count):]
            break

    for stack in range(1, len(stacks)+1):
        result += stacks[stack][0]

    print(result)


if __name__ == "__main__":
    part1()
    part2()