# ----------------------------------------------------------
# --------------- Strings Indexing & Slicing ---------------
# [1] All data in Python is Object
# [2] Object contain elements
# [3] Every element has its own index
# [4] Python use zero based indexing (index start from zero)
# [5] Use square brackets to access element
# [6] Enable accessing parts of Strings, Tuples of Lists
# ----------------------------------------------------------

# Indexing (Access single item)
myString = "I love Python"
print(myString[0])  # Index 0 => I
print(myString[9])  # Index 9 => t

print(myString[-1])  # Index -1 => First character from end => n
print(myString[-6])  # Index -6 => 6th character from end => P

# Slicing ( Access multiple sequence items )
# [start:end]
# [start:end:steps]
print(myString[8:11])  # yth
print(myString[3:5])  # ov

print(myString[:10])  # If start is not assigned will start from 0 (I love Pyt)
print(myString[5:])  # If end is not assigned will will go to the end (e Python)
print(myString[:])  # Full Data

print(myString[0::1])  # Full Data
print(myString[::1])  # Full Data
print(myString[::2])
print(myString[::3])
