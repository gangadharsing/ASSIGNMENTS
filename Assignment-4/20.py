# 20.  Write a Python program to remove all consecutive duplicates of a given string.

class Solution:
  def solve(self, s):
      seen = s[0]
      ans = s[0]
      for i in s[1:]:
         if i != seen:
            ans += i
            seen = i
      return ans
ob = Solution()
str=input("Enter the string : ")
print(ob.solve(str))