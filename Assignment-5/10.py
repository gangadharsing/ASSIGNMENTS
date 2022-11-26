# 10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = eval(input("Enter your salary:"))
service_yrs = eval(input("Enter Years of service:"))
if service_yrs > 5:
    print("Yours salary(+Bonus) = ",salary + (salary)*5/100)
else:
     print("You are not eligible for bonus as you have less service years.")

