from utils import process_input_to_list
from typing import List


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


def main():
    inputList = process_input_to_list('input.txt')
    two_sum = process_list_two_sum(inputList, 2020)
    three_sum = process_list_three_sum(inputList, 2020)
    print(three_sum)


if __name__ == '__main__':
    main()
