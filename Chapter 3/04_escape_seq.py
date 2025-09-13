a = "Nishant is good boy\nbut not bad boy"
print(a) 


# 🔹 Common Escape Sequences

# \n → New line

# print("Hello\nWorld")
# # Output:
# # Hello
# # World


# \t → Tab (adds horizontal space)

# print("Hello\tWorld")
# # Output: Hello    World


# \\ → Backslash (\)

# print("This is a backslash: \\")
# # Output: This is a backslash: \


# \' → Single quote

# print('It\'s Python')
# # Output: It's Python


# \" → Double quote

# print("He said \"Hello\"")
# # Output: He said "Hello"

# 🔹 Less Common but Useful

# \r → Carriage return (cursor goes to beginning of line)

# print("Hello\rWorld")
# # Output: World


# \b → Backspace (removes previous character)

# print("Helloo\b")
# # Output: Hello


# \f → Form feed (new page – rarely used, behaves like \n)

# print("Hello\fWorld")


# \a → Bell (alert sound – not always noticeable on all systems)

# print("\a")  

# 🔹 Unicode & Octal

# \ooo → Octal value

# print("\101")   # Output: A


# \xhh → Hexadecimal value

# print("\x41")   # Output: A


# \uXXXX → Unicode (16-bit)

# print("\u03A9")   # Output: Ω


# \UXXXXXXXX → Unicode (32-bit)

# print("\U0001F600")   # 😀