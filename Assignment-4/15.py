# 15. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

import collections
string1 = input("enter the string")
d=collections.defaultdict(int)

for x in string1:
    d[x] += 1
for i in sorted(d,key=d.get,reverse = True):
    if  d[i] >1:
        print('%s %d' % (i,d[i]))
