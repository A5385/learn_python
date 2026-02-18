# --------------------------------
# --- Strings Methods (part I) ---
# --------------------------------
# [1] len() => get string length
# [2] strip() rstrip() lstrip() => remove space ( by default if not add certain value) and r from right and l from left and without r/l form both
# [3] title() => convert first char to uppercase and the char after number to uppercase
# [4] Capitalize() => Convert first char to uppercase
# [5] zfill
# [6] upper()
# [7] lower()
# [8] split() rsplit() => by default split elements by space unless you assign specific char and return list of element
# [9] center() => take 2 args 1st is mandatory the number of char 2nd is optional and by default white space " " and you can specify char like $ #
# [10] count()
# [11] swapcase()
# [12] startswith()
# [13] endswith()
# [14] index(SubString, Start, End) => SubString is mandatory, start and end is optional
# [15] find(SubString, Start, End) => SubString is mandatory, start and end is optional
# [16] rjust(width, fill char) lJust(width, fill char) => width is mandatory, fill char is optional and add " " by default
# [17] splitlines() => return list separate by new line
# [18] expandtabs()
# [19] istitle() => return boolean
# [20] isspace() => return boolean
# [21] islower() => return boolean
# [22] isidentifier => return boolean
# [23] isalpha() => return boolean
# [24] isalnum => return boolean
# [25] replace(old value, new value, count)
# [26] join(Iterable)

a = "I Love Python"
b = "        I Love Python         "

# [1] len() => get string length
print(len(a))
print(len(b))

# [2] strip() rstrip() lstrip() => remove space ( by default if not add certain value) and r from right and l from left and without r/l form both
print(b.strip())  # => I Love Python
print(b.rstrip())  # => I Love Python
print(b.lstrip())  # =>         I Love Python

b = "#########I Love Python#########"
print(b.strip("#"))  # => I Love Python
print(b.rstrip("#"))  # => I Love Python
print(b.lstrip("#"))  # =>         I Love Python

b = "@@###I Love Python@@###$"
print(b.strip("#@$"))  # => I Love Python
print(b.rstrip("#@"))  # => I Love Python
print(b.lstrip("#@"))  # =>         I Love Python

c = "i love 2d Graphics and 3g Technology and python"
# [3] title() => convert first char to uppercase and the char after number to uppercase
print(c.title())

# [4] Capitalize() => Convert first char to uppercase
print(c.capitalize())

# [5] zfill
c, d, e, f = "1", "11", "111", "1111"
print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# [6] upper()
g = "ahmed"
print(g.upper())

# [7] lower()
g = "OSAMA"
print(g.lower())


# [8] split() rsplit() => by default split elements by space unless you assign specific char and return list of element

a = "I Love Python and PHP"
print(a.split())
print("{type(a.split())}")

a = "I-Love-Python-and-PHP"
print(a.split("-"))

a = "I-Love-Python-and-PHP"
print(a.split("-", 2))


print(a.rsplit("-", 2))

# [9] center() => take 2 args 1st is mandatory the number of char 2nd is optional and by default white space " " and you can specify char like $ #

b = "Ahmed"
print(b.center(9))
print(b.center(9, "~"))

# [10] count()
c = "I Love Python because Python is easy"
print(c.count(" "))
print(c.count("Python"))
print(c.count("Python", 0, 13))

# [11] swapcase()
d = "I Love Python"
e = "i lOVE pYTHON"
print(d.swapcase())
print(e.swapcase())

# [12] startswith()
d = "I Love Python"
print(d.startswith("I"))
print(d.startswith("S"))

print(d.startswith("P", 7, 12))

# [13] endswith()
e = "I Love Python"
print(e.endswith("n"))
print(e.endswith("N"))
print(e.endswith("e", 2, 6))

# [14] index(SubString, Start, End) => SubString is mandatory, start and end is optional
a = "I Love Python"

print(a.index("P"))  # Index Number 7
print(a.index("P", 0, 10))  # Index Number 7
# print(a.index("P", 0, 5)) # Through Error

# [15] find(SubString, Start, End) => SubString is mandatory, start and end is optional
b = "I Love Python"

print(b.find("P"))  # Index Number 7
print(b.find("P", 0, 10))  # Index Number 7
print(b.find("P", 0, 5))  # -1

# [16] rjust(width, fill char) lJust(width, fill char) => width is mandatory, fill char is optional and add " " by default

c = "Ahmed"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "Ahmed"
print(d.ljust(10))
print(d.ljust(10, "#"))

# [17] splitlines() => return list separate by new line

e = """First Line
Second Line
Third Line"""

print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"
print(f.splitlines())

# [18] expandtabs()

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(1))


# [19] istitle() => return boolean
one = "I Love Python And 3G"
two = "I love Python And 3g"
print(one.istitle())
print(two.istitle())

# [20] isspace() => return boolean
three = " "
four = ""
print(three.isspace())
print(four.isspace())

# [21] islower() => return boolean
five = "i love python"
six = "I Love Python"
print(five.islower())
print(six.islower())

# [22] isidentifier => return boolean


seven = "osama_elzero"
eight = "osamaElzero100"
nine = "osama--Elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

# [23] isalpha() => return boolean

x = "AaaaaBbbbb"
y = "AaaaaBbbbb111"
print(x.isalpha())
print(y.isalpha())

# [24] isalnum => return boolean

u = "AaaaaBbbbb"
z = "AaaaaBbbbb111"
i = "66544454"
e = "#######"
print(u.isalnum())
print(z.isalnum())
print(i.isalnum())
print(e.isalnum())

# [25] replace(old value, new value, count)
a = "Hello One Two Three One One"
print(a.replace("One", "1"))
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))

# [26] join(Iterable)
myList = ["Ahmed", "Osama", "Khaled"]
print("-".join(myList))
print(" ".join(myList))
print(", ".join(myList))
print(type(", ".join(myList)))
