# 10. Write a Python program to get the class name of an instance in Python.

class class_name:
    def name(self, name):
        return name
v = class_name()
print(v.__class__.__name__)
