# A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.

word = "donkey"

with open("E:\Fortune Cloud WD\Python\Chapter 9\don.txt","r") as f:
    content = f.read()

contentNew = content.replace(word,"#####")

with open("don.txt","w") as f:
    f.write(contentNew)