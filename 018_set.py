# -----------------------------
# ------------ Set ------------
# -----------------------------
# [1] Set items are enclosed in curly braces
# [2] Set items are not ordered and not indexed
# [3] Set indexing and slicing cannot be done
# [4] Set has only immutable data types (numbers, strings, tuples) list and dict are not
# [5] Set Items is unique
# -----------------------------

# [1] Set items are enclosed in curly braces
mySetOne = {"Ahmed", "Khaled", 100}
print(mySetOne)

# [2] Set items are not ordered and not indexed
# print(mySetOne[0]) # Error => 'set' object is not subscriptable

# [3] Set indexing and slicing cannot be done
mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3]) # Error => 'set' object is not subscriptable

# [4] Set has only immutable data types (numbers, strings, tuples) list and dict are not
# mySetThree = {"Osama",100,100.5,True,[1,2,3]} # Error => cannot use 'list' as a set element (unhashable type: 'list')
mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)}
print(mySetThree)

# [5] Set Items is unique
mySetFour = {1, 2, "Osama", "One", "Osama", 1}
print(mySetFour)  # will cancel 1 and Osama
