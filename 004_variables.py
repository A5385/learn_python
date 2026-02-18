# -------------------------------------------------------
# ------------------- Variables -------------------------
# -------------------------------------------------------
# Syntax => [Variable Name] [Assignment Operator] [Value]
# -------------------------------------------------------
# Name Convention and Roles
# [1] Can start with (a-z A-Z) or Underscore
# [2] you cannot start with num or special characters
# [3] Can Include (0-9) Or Underscore
# [4] Cannot Include Special Characters
# [5] Name is Not Like name [ Case Sensitive ]
# [6] Cannot use variable before assign
# -------------------------------------------------------

myVariable = "My Value"
my100_Variable = "My Value"
print(myVariable)

# best practice naming variables
name = "Ahmed Khaled"  # Single word => Normal
myName = "Ahmed Khaled"  # Two words => camelCase
my_name = "Ahmed Khaled"  # Two words => snake_case

# Source Code : Original code you write it in computer
# Translation : Converting source code into machine language
# Compilation : Translate code before run time
# Run-Time : Period app take to executing commands
# Interpreted : Code translated on the fly during execution


# Python => is dynamically typed language

x = 10
x = "Hello"

print(x)

# we can know the reserved keywords by type
help("keywords")

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
