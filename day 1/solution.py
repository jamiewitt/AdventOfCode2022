import sys
sys.path.append( '../' )

from utils import profiler

@profiler
def part1():
    file1 = open('input.txt', 'r')

    lines = file1.readlines()

    elf_num = 1
    calories = 0
    max_calories = 0

    for line in lines:
        if len(line.strip()) == 0:
            if calories > max_calories:
                max_calories = calories
            elf_num += 1
            calories = 0
            continue
        calories += int(line.strip())

    print(max_calories)

@profiler
def part2():
    file1 = open('input.txt', 'r')

    lines = file1.readlines()

    elf_num = 1
    calories = 0
    max_calories = []

    for line in lines:
        if len(line.strip()) == 0:
            if len(max_calories) < 3:
                max_calories.append(calories)
                max_calories.sort()
            elif calories > max_calories[0]:
                max_calories.pop(0)
                max_calories.append(calories)
                max_calories.sort()
            elf_num += 1
            calories = 0
            continue
        calories += int(line.strip())

    print(sum(max_calories))

if __name__ == "__main__":
    part1()
    part2()