# write  a program to find out whether a student passed or failed if it requires a total of 40% and at least 33% in each subject to pass.assume 3 subject and take marks as an input from user. 

m1 = int(input("Enter subject 1 marks :"))
m2 = int(input("Enter subject 2 marks :"))
m3 = int(input("Enter subject 3 marks :"))

total_percentage = (100*(m1 + m2 + m3))/300  # sum of the marks multiply by 100 and divided by 100

if total_percentage >= 40 and m1 > 33 and m2 > 33 and m3 > 33:
    print(f"You are pass",total_percentage)

else:
    print(f"You are fail,try again next year",total_percentage)