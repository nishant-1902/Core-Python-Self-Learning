# write a python program which converts inches to cms
def inch_to_cm(inch):
    return inch * 2.54
n = int(input("Enter value in inches :"))
print(f"the corresponding value in cms is :{inch_to_cm(n)}")