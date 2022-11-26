# 9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

price=int(input("enter price"))
qty=int(input("enter quantity"))
amt=price*qty
if amt>1000:
   print ("10% discount applicable")
   discount=amt*10/100
   amt=amt-discount
   print ("amount payable:",amt)
else:
   print("amount payable:",amt)
