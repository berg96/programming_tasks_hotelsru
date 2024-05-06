from typing import Optional


def get_common_divisors(numbers: list[int]) -> Optional[list[int]]:
    result = []
    divisors_of_min_num = []
    min_num = min(numbers)
    if min_num > 1:
        for divisor in range(2, min_num + 1):
            if min_num % divisor == 0:
                divisors_of_min_num.append(divisor)
    else:
        return [1]
    for divisor in divisors_of_min_num:
        count = 0
        for number in numbers:
            if number % divisor == 0:
                count += 1
        if count == len(numbers):
            result.append(divisor)
    return result


if __name__ == '__main__':
    print(get_common_divisors(list(map(int, input().split()))))
