ROMAN = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
OPERANDS = '+-*/'
LEFT_BORDER = 1
RIGHT_BORDER = 100


def arabic_calc(num1, operand, num2):
    if operand == '+':
        result = num1 + num2
    elif operand == '-':
        result = num1 - num2
    elif operand == '*':
        result = num1 * num2
    elif operand == '/':
        result = int(num1 / num2)

    return result


def roman_to_arabic(roman):
    result = 0
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and ROMAN[roman[i]] < ROMAN[roman[i + 1]]:
            result -= ROMAN[roman[i]]
        else:
            result += ROMAN[roman[i]]

    return result


def arabic_to_roman(arabic):
    arabic = str(arabic)
    romans = list(ROMAN)
    str_arabic = arabic[::-1]
    str_arabic_len = len(str_arabic)
    result = str()
    romans_pointer = 0

    for i in range(str_arabic_len):
        print(int(str_arabic[i]))
        if str_arabic[i] in ['0', '1', '2', '3']:
            result = romans[romans_pointer] * int(str_arabic[i]) + result
        elif str_arabic[i] in ['4']:
            result = romans[romans_pointer] + romans[romans_pointer + 1] + result
        elif str_arabic[i] in ['5', '6', '7', '8']:
            result = romans[romans_pointer + 1] + romans[romans_pointer] * (int(str_arabic[i]) - 5) + result
        elif str_arabic[i] in ['9']:
            result = romans[romans_pointer] + romans[romans_pointer + 2] + result
        romans_pointer += 2

    return result


def numbers_check(num1, num2):
    left_border = LEFT_BORDER
    right_borrder = RIGHT_BORDER
    return left_border <= num1 <= right_borrder and left_border <= num2 <= right_borrder


def roman_check(num):
    checks = [el in ROMAN for el in num]
    return all(checks)


def calculate(string):
    symbols_list = string.split()

    if len(symbols_list) < 3:
        return 'The string you entered contains not enough values.'

    elif len(symbols_list) > 3:
        return 'The string you entered contains too many values.'

    num1 = symbols_list[0]
    num2 = symbols_list[2]
    operand = symbols_list[1]

    if operand not in OPERANDS:
        return 'There is no operand like this'

    elif num1.isdigit() and num2.isdigit():
        num1, num2 = int(num1), int(num2)

        if numbers_check(num1, num2):
            return arabic_calc(num1=num1, operand=operand, num2=num2)
        else:
            return 'One or both numbers are not in the specified numeric range.'

    elif roman_check(num1) and roman_check(num2):
        num1, num2 = roman_to_arabic(num1), roman_to_arabic(num2)

        if numbers_check(num1, num2):
            if num1 <= num2 and operand == '-':
                return 'There are no negative numbers (and zero) in the Roman numeral system.'
            return arabic_to_roman(arabic_calc(num1=num1, operand=operand, num2=num2))
        else:
            return 'One or both numbers are not in the specified numeric range.'

    elif roman_check(num1) and num2.isdigit() or \
            roman_check(num2) and num1.isdigit():
        return 'Numbers in different number systems.'

    else:
        return 'Something wrong with entered string.'


if __name__ == '__main__':
    while True:
        user_string = input()
        result = calculate(user_string)
        print(result)
