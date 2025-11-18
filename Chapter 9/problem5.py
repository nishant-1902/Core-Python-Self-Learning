# 5. Repeat program 4 for a list of such words to be censored.

word = ["donkey","bad","ganda"]

with open("E:\Fortune Cloud WD\Python\Chapter 9\don.txt","r") as f:
    content = f.read()

for word in word:
    content = content.replace(word,"#" * len(word))

with open("don.txt","w") as f:
    f.write(content)