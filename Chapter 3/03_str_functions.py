name = "nishant"
print(len(name))

print(name.endswith("ant"))

print(name.startswith("n"))

print(name.capitalize())

print(name.isalnum())

print(name.isalpha())

print(name.isdigit())


# Case Conversion Functions

# upper() → Converts all characters to uppercase.

# "hello".upper()   # "HELLO"


# lower() → Converts all characters to lowercase.

# "HELLO".lower()   # "hello"


# title() → Converts the first letter of each word to uppercase.

# "python programming".title()   # "Python Programming"


# capitalize() → Capitalizes only the first letter of the string.

# "python".capitalize()   # "Python"


# swapcase() → Swaps case (upper → lower, lower → upper).

# "PyThOn".swapcase()   # "pYtHoN"


# 🔹 Searching & Checking

# find(sub) → Returns index of first occurrence (or -1 if not found).

# "hello".find("l")   # 2


# rfind(sub) → Returns index of last occurrence.

# "hello".rfind("l")   # 3


# index(sub) → Like find(), but raises an error if not found.

# "hello".index("e")   # 1


# startswith(prefix) → Checks if string starts with given value.

# "python".startswith("py")   # True


# endswith(suffix) → Checks if string ends with given value.

# "python".endswith("on")   # True

# 🔹 Testing String Content

# isalnum() → Returns True if string is alphanumeric.

# "abc123".isalnum()   # True


# isalpha() → Returns True if all characters are alphabets.

# "hello".isalpha()   # True


# isdigit() → Returns True if all characters are digits.

# "123".isdigit()   # True


# isspace() → Returns True if string contains only spaces.

# "   ".isspace()   # True


# islower() / isupper() / istitle() → Check case.

# "hello".islower()   # True

# 🔹 Modification & Replacing

# strip() → Removes spaces (or characters) from both ends.

# "  hello  ".strip()   # "hello"


# lstrip() → Removes spaces from left side.

# "  hello".lstrip()   # "hello"


# rstrip() → Removes spaces from right side.

# "hello  ".rstrip()   # "hello"


# replace(old, new) → Replaces substring.

# "hello world".replace("world", "Python")   # "hello Python"

# 🔹 Splitting & Joining

# split() → Splits string into list (by spaces or given separator).

# "a,b,c".split(",")   # ['a', 'b', 'c']


# rsplit() → Splits from the right side.

# "a,b,c".rsplit(",", 1)   # ['a,b', 'c']


# splitlines() → Splits by line breaks.

# "hello\nworld".splitlines()   # ['hello', 'world']


# join(iterable) → Joins elements with a string.

# "-".join(["a", "b", "c"])   # "a-b-c"

# 🔹 Formatting

# format() → Used for string formatting.

# "My name is {}".format("Nishant")   # "My name is Nishant"


# zfill(width) → Pads string with zeros in front.

# "7".zfill(3)   # "007"