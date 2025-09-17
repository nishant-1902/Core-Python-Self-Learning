# if elif else ladder

a = int(input("Enter age :"))
if a > 18:
    print("Your age is above the consent")

elif a < 0:
    print("You are entering invalid age")

elif a == 0:
    print("Your age is 0 it is not valid")    
    
else:
    print("Your age below the consent")     

print("end the program")