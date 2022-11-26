# 19.  Write a Python program to find smallest and largest word in a given string.

sentence = input("Enter the String: ")
print("\nLargest Word(s): ")
word=[len(k) for k in sentence.split()]
print(*[i for i in sentence.split() if len(i) == max(word)])
print("\nSmallest Word(s): ")
print(*[i for i in sentence.split() if len(i) == min(word)])