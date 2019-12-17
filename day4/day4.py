"""day4.py
Input: 168630-718098
"""

def increase_check(num):
    num = str(num)
    for i in range(len(num)-1):
        if int(num[i]) > int(num[i+1]):
            return False
    return True

def doubles_check(num):
    num = str(num)
    for i in range(len(num)-1):
        if int(num[i]) == int(num[i+1]):
            return True
    return False

def part2_check(num):
    num = str(num)
    for digit in num:
        count = num.count(digit)
        if count == 2 or count == 4:
            return True
    return False

if __name__ == '__main__':
    low = 168630
    high = 718098
    increase_list = [num for num in range(low, high+1) if increase_check(num)]
    password_list = [num for num in increase_list if doubles_check(num)]
    part2_list = [num for num in password_list if part2_check(num)]
    print(f'Part 1: The number of potential passwords is {len(password_list)}.')
    print(f'Part 2: The number of potential passwords is {len(part2_list)}.')
