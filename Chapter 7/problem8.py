#  write a program to print following star pattern 
#   *
#   **
#   ***

num = int(input("Enter a number :"))
for i in range(1,num+1):
    print("*"*i,end="")
    print(" ")