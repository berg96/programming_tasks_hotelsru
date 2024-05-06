import pymorphy2


def declension_computer_with_morph(number: int) -> str:
    morph = pymorphy2.MorphAnalyzer()
    return (
        f'{number} '
        f'{morph.parse("компьютер")[0].make_agree_with_number(number).word}'
    )


def declension_computer(number: int) -> str:
    if number % 10 == 1 and number % 100 != 11:
        return f'{number} компьютер'
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
        return f'{number} компьютера'
    else:
        return f'{number} компьютеров'


if __name__ == '__main__':
    print(declension_computer(int(input())))
    print(declension_computer_with_morph(int(input())))
