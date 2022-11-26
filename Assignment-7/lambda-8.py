# 8. Write a Python program to check whether a given string contains a capital letter,
# a lower case letter, a number and a minimum length using lambda.
# Minimum length : 10 input string: PaceWisd0m o/p: valid string

def check(str1):
    a = [
    lambda str1: any(x.isupper() for x in str1) or 'String must have 1 upper case .',
    lambda str1: any(x.islower() for x in str1) or 'String must have 1 lower case .',
    lambda str1: any(x.isdigit() for x in str1) or 'String must have 1 number.',
    lambda str1: len(str1) >= 7                 or 'String length should be atleast 8.',]
    result = [x for x in [i(str1) for i in a] if x != True]
    if not result:
        result.append('Valid string.')
    return result
s = input("Input the string:")
print(check(s))


