# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’.

f = open("E:\Fortune Cloud WD\Python\Chapter 9\poem.txt")
content = f.read()
if ("twinkle" in content):
    print("The word twinkle present in the content")
else:
    print("The word twinkle not present in the content")    