# 8. Write a python class which has 2 methods get_string and print_string.
# get_string takes a string from the user and print_string prints the string in reverse order

class reverse():
    def __init__(self):
        self.str1 = ''
    def get_String(self):
        self.str1 = input('enter the value')
    def print_String(self):
        return ''.join(reversed(self.str1))
str1 = reverse()
str1.get_String()
print(str1.print_String())