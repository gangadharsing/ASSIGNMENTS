# 7. Write a Python class to reverse a string word by word.
# Input string : 'hello .py' Expected Output : '.py hello'

class reverse:
    def revwords(self, s):
        return ' '.join(reversed(s.split()))
print(reverse().revwords('hello .py'))