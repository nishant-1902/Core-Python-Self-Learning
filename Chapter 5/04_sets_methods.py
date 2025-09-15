s = {1,2,3,4,5,6}
p = {1,2}
print(type(s))

s.add(7)  # add element in a set
print(s)


print(s.union(p)) # return all items in both sets

print(s.intersection(p)) # return the same values in both sets

print(s.issubset(p)) 

print(s.issuperset(p))

print(s.isdisjoint(p))

