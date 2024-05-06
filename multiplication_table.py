def multiplication_table(number: int) -> None:
    table = [['' for _ in range(number + 1)] for _ in range(number + 1)]
    for row in range(number + 1):
        for colum in range(number + 1):
            if row == 0 or colum == 0:
                table[row][colum] = str(row + colum)
            else:
                table[row][colum] = str(row * colum)
    table[0][0] = ' '
    for row in range(number + 1):
        print(' '.join(table[row]))


if __name__ == '__main__':
    multiplication_table(int(input()))
