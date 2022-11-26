# 14. Print multiplication table of 24, 50 and 29 using loop.

for i in [24,29,50]:
 print(f"Multiplication table of {i}:")
 for j in range(1,11):
   print(f"{i} * {j} = {i*j}")
 print()


