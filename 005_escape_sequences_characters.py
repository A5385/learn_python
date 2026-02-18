# -------------------------------
# Escape Sequences Characters
# -------------------------------
# \b => Back space
# \newline => Escape new line +\
# \\ => escape back slash
# \' => escape single quote
# \" => escape double quote
# \n => Line Feed
# \r => Carriage return
# \t => horizontal tab
# \xhh => character hex value
# -------------------------------

# Back space
print("Hello\bWorld")  # <= will remove o

# Escape New Line + \
print(
    "Hello \
I \
Love \
Python"
)

# Escape Back Slash
print("I Love Back Slash \\")

# Escape Single Quote
print("I Love Single Quote 'Test' ")

# Escape Double Quotes
print('I Love Single Quotes "Test" ')

# Line Feed
print("Hello world\nsecond line")

# Carriage Return
print("123456\rAbcd")

# horizontal tab
print("Hello\tPython")

# Character Hex Value
print("\x2a")  # print o
