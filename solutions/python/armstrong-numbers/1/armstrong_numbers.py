def is_armstrong_number(number):
    string = str(number)
    sum = 0
    length = len(string)

    for ch in string:
        sum += int(ch) ** length

    return sum == number
