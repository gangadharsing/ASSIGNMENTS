# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
# Sample String : 'thisisniceone'
# Expected Result : 'thne”'
def string_both_ends(str):
  if len(str) < 2:
    return ''
  return str[0:2] + str[-2:]
str=input("Enter the string :")
print(string_both_ends(str))

# Sample String : 'ab'
# Expected Result : 'abab'
def string_both_ends(str):
  if len(str) < 2:
    return ''
  return str[0:2] + str[-2:]
print(string_both_ends('ab'))

# Sample String : 'f'
# Expected Result : Empty String
def string_both_ends(str):
  if len(str) < 2:
    return ''
  return str[0:2] + str[-2:]
print(string_both_ends('f'))
