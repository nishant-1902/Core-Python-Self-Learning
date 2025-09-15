#   create mepty dictionary allow 4 frnds to enter their fav lang as value and use key as their names. Assume that the names are unique
s = {}

name = input("Enter name :")
lang = input("Enter language :")
s.update({name:lang})

name = input("Enter name :")
lang = input("Enter language :")
s.update({name:lang})

name = input("Enter name :")
lang = input("Enter language :")
s.update({name:lang})

name = input("Enter name :")
lang = input("Enter language :")
s.update({name:lang})

print(s)