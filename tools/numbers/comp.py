"""
comp.py i have here two complex functions.
the first function shows me a number and adds up
the digits of the numbers

the second function gets a number and tells me if the number is a
palindrome or not
"""

#making a function that takes which ever digits i want to give her
#and making it add up the numbers within the digit
def sum_of_digit(num): 
    digits = str(num) 
    digit_sum = 0 
    for digit in digits:
        digit_sum += int(digit)
    return digit_sum

# total = sum_of_digit (1864)
# print(total)

#taking whatever number i want and cheking if the num is
#a palindrome
def ispal(num):
    num_str = str(num)
    reversed_str = num_str[::-1]
    if num_str == reversed_str:
        return True
    else:
        return False

#cheking if number is a palindrom
# print(ispal(565)) #true exemple 
# print(ispal(563)) #false exemple

