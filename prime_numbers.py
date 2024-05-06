from typing import Optional


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def prime_numbers_in_range(min_num: int, max_num: int) -> Optional[list[int]]:
    prime_numbers = []
    for number in range(min_num, max_num + 1):
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers


if __name__ == '__main__':
    print(prime_numbers_in_range(min_num=int(input()), max_num=int(input())))
