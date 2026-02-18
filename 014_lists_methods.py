# ------------------------------
# --- Lists Methods - Part I ---
# ------------------------------
# [1] append()
# [2] extends()
# [3] remove()
# [4] sort()
# [5] reverse()
# [6] clear()
# [7] copy()
# [8] count()
# [9] index()
# [10] insert()
# [11] pop()
# ------------------------------

# [1] append()
myFriends = ["Ahmed", "Osama", "Sayed"]
myOldFriends = ["Mahmoud", "Mohamed", "Moamen"]

myFriends.append("Hassan")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends)

print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7][2])

# [2] extends()
a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)
print(a)

# [3] remove()
x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
x.remove("Osama")
print(x)

# [4] sort()
y = [1, 2, 100, 120, -10, 17, 29]
y.sort()
print(y)
y.sort(reverse=True)
print(y)

# [5] reverse()
z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z)


# [6] clear()
a = [1, 2, 3, 4]
a.clear()
print(a)

# [7] copy()
b = [1, 2, 3, 4]
c = b.copy()

print(b)
print(c)

b.append(5)
print(b)
print(c)

# [8] count()
d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# [9] index()
e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

# [10] insert()
f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(4, "C")
f.insert(-1, "Test")
print(f)


# [11] pop()
g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(2))
