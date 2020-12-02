from typing import List


def process_input_to_list(filename: str) -> List[int]:
    with open(filename) as f:
        lst = [int(x) for x in f.read().split()]
    return lst
