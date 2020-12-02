import timeit
import statistics
from typing import List


def process_input_to_list(filename: str) -> List[int]:
    with open(filename) as f:
        lst = [int(x) for x in f.read().split()]
    return lst


def process_list_two_sum(inputList: List[int],
                         magic_num: int) -> int:
    cache = set()
    for i, num in enumerate(inputList):
        target = magic_num - num
        if target in cache:
            return num * target
        cache.add(num)


def process_list_three_sum(inputList: List[int],
                           magic_num: int) -> int:
    list_size = len(inputList)
    for i in range(0, list_size-1):
        cache = set()
        middle_target = magic_num - inputList[i]
        for j in range(i + 1, list_size):
            final_target = middle_target - inputList[j]
            if (final_target in cache):
                return inputList[i] * inputList[j] * final_target
            cache.add(inputList[j])


def testspeed(part: str) -> float:
    test_map = {
        'part1': {
            'setup': '''from __main__ import process_list_two_sum, process_input_to_list\ninputList = process_input_to_list('input.txt')''',
            'stmt': '''process_list_two_sum(inputList, 2020)'''
        },
        'part2': {
            'setup': '''from __main__ import process_list_three_sum, process_input_to_list\ninputList = process_input_to_list('input.txt')''',
            'stmt': '''process_list_three_sum(inputList, 2020)'''
        }
    }
    reps = timeit.repeat(repeat = 1000,
                         number = 1,
                         stmt=test_map[part]["stmt"],
                         setup=test_map[part]["setup"])
    return statistics.mean(reps) * 1000


def part1(inputList):
    two_sum = process_list_two_sum(inputList, 2020)
    speed = testspeed('part1')
    print('Part One: {} -- {:0.2f} ms'.format(two_sum, speed))

def part2(inputList):
    three_sum = process_list_three_sum(inputList, 2020)
    speed = testspeed('part2')
    print('Part Two: {} -- {:0.2f} ms'.format(three_sum, speed))

if __name__ == '__main__':
    inputList = process_input_to_list('input.txt')
    part1(inputList)
    part2(inputList)
