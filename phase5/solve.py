from typing import List

values = [15, 0, 5, 11, 13, 1]


def get_valid_chars(x: int) -> List[str]:
    valid = []
    for i in range(32, 122, 1):
        if i & 0xF == x:
            valid.append(chr(i))
    return valid


for i in values:
    print(get_valid_chars(i))
