Mark1=float(input("Enter your Marks for 1:"))
Mark2=float(input("Enter your Marks for 2:"))
Mark3=float(input("Enter your Marks for 3:"))
Avg=(Mark1+Mark2+Mark3)/3
print("Your total aggregate mark is %.2f" % (Avg))
if(Avg>=90 and Mark1 >= 50 and Mark2 >= 50 and Mark3 >= 50):
    print("Excellent You got A+. Now go play Games")
elif(Avg>=80 and Mark1 >= 50 and Mark2 >= 50 and Mark3 >= 50):
    print("Good You got B. Now go play Games")
elif(Avg>=70 and Mark1 >= 50 and Mark2 >= 50 and Mark3 >= 50):
    print("Not Bad You got C. Now go play Games")
elif(Avg>=60 and Mark1 >= 50 and Mark2 >= 50 and Mark3 >= 50):
    print("Keep Trying You got D. Now go play Games")
elif(Avg>=50 and Mark1 >= 50 and Mark2 >= 50 and Mark3 >= 50):
    print("You got E. No Game for u")
else:
    print("You got F. No Game for u")