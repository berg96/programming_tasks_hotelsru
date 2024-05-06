def multiplication_table(number: int) -> None:
    table = [['' for _ in range(number + 1)] for _ in range(number + 1)]
    len_max_num = len(str(number * number))
    for row in range(number + 1):
        for column in range(number + 1):
            if row == 0 or column == 0:
                table[row][column] = str(row + column).rjust(len_max_num)
            else:
                table[row][column] = str(row * column).rjust(len_max_num)
    table[0][0] = ''.rjust(len_max_num)
    for row in range(number + 1):
        print(' '.join(table[row]))


if __name__ == '__main__':
    multiplication_table(int(input()))
