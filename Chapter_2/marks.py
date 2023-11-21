marks = int (input("enter the marks "))

# between 81 and 100
if marks >= 80:
    print("Very Good")

#between 61 and 80
elif (marks > 60):
    print("Good")

#between 41 and 60 
elif (marks > 40):
    print("Average")

# less than or equal to 40
else:
    print("Fail")