# 2. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(tuples)
tuples.sort(key = lambda x: x[1])
print("Sorting the List of Tuples:")
print(tuples)

