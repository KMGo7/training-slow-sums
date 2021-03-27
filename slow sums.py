
"""



"""


import math
import array


# Add any extra import statements you may need here


# Add any helper functions you may need here


def getTotalTime(arr):
    if len(arr) < 2:
        return 0;
    temp1 = 0
    temp2 = 0
    sum_penalty = 0
    sorted_arr = sorted(arr)
    print(sorted_arr)
    while len(sorted_arr) > 1:
        temp1 = sorted_arr.pop()
        temp2 = sorted_arr.pop()
        penalty = temp1+temp2
        sum_penalty += penalty
        sorted_arr.append(penalty)
    return sum_penalty


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    arr_1 = [4, 2, 1, 3]
    expected_1 = 26
    output_1 = getTotalTime(arr_1)
    check(expected_1, output_1)

    arr_2 = [2, 3, 9, 8, 4]
    expected_2 = 88
    output_2 = getTotalTime(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
