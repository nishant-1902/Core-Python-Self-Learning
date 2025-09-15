marks = {
    "Nishant" : 100,
    "shubham" : 98,
    "rohan" : 23
}

# print(marks.items()) # return a list of item (key,value) in dict

# print(marks.keys()) # return the keys of dictionary

# print(marks.values()) # return the values of dictionary 

marks.update({"Nishant":99})  # update the dictionary
print(marks)

print(marks.get("rohan")) # return the value of specified keys