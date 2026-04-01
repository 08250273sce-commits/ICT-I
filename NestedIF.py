age=int(input("Enter your age:"))
if age>=18:
    registered_voter=input("Are you a regidtered voter?(True/False):")
    registered_voter=registered_voter.lower()  # Convert input to lowercase for consistency
    if registered_voter=="true":
        print("You are eligible to vote.")
    else:
        print("You need to be a registered voter to vote.")
else:    
    print("You are not eligible to vote yet. You must be at least 18 years old.")