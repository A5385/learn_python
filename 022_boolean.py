# -------------------------------------------------------------------------
# -------------------------------- Boolean --------------------------------
# -------------------------------------------------------------------------
# [1] In programming you need to know if your code output is True or False
# [2] Boolean values are the two constant objects False + True
# -------------------------------------------------------------------------

# Logical
name = ""
print(name.isspace())

name = " "
print(name.isspace())
print("-" * 50)  ###### Separator

print(100 > 200)
print(100 > 100)
print(100 > 90)

print("-" * 50)  ###### Separator
# True Values
print(bool("Osama"))
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

print("-" * 50)  ###### Separator
# False Values
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))
print(bool(False))
