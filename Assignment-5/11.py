# 11. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

score = input("Enter your score")
score = int(score)
if score < 25:
   print("F")
elif score >= 25 and score < 45:
   print("E")
elif score >= 45 and score < 50:
   print("D")
elif score >= 50 and score < 60:
   print("C")
elif score >= 60 and score < 80:
   print("B")
else:
   print("A")
