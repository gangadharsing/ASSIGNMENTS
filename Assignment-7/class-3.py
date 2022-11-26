# 3. Write a Python class to get all possible unique subsets from a set of distinct integers
# Input : [4, 5, 6] Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]


from itertools import combinations
line=sorted(input().split())
length = len(line)
for i in range(1,length+1):
    words=combinations(line,i)
    words=sorted(words)
    words=set(words)
    for j in list(sorted(words)):
        print(j)
