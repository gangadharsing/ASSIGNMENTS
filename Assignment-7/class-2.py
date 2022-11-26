# 2. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and
# "{{{" are invalid.

class solution:
   def parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
print(solution().parenthese("(){}[]"))
print(solution().parenthese("()[{)}"))
print(solution().parenthese("()"))
print(solution().parenthese("{{{"))

