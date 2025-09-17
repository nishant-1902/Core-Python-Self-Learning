a = int(input("Enter age :"))
 
# if statement : 1 
if a % 2 == 0:
    print("is even")
# if statement : 2 
if a > 18:
    print("Your age is above the consent")

elif a < 0:
    print("You are entering invalid age")

elif a == 0:
    print("Your age is 0 it is not valid")    
    
else:
    print("Your age below the consent")     

print("end the program")