# -----------------------------------------------------------
# ---------------------- Tuple Methods ----------------------
# -----------------------------------------------------------
# [1] Concatenation
# [2] count()
# [3] index()
# [4] Tuple Destruct
# -----------------------------------------------------------

# [1] Concatenation
a = (1,2,3,4)
b = (5,6)

c = a + b
d = a + ("A","B",True) + b

print(c)
print(d)

# [2] count()
a = (1,3,7,8,2,6,5,8)
print(a.count(8))

# [3] index()
b= (1,3,7,8,9)
# print("The position of index is: " + b.index(7)) # error
print(f"The position of index is: {b.index(7)}") 

# [4] Tuple Destruct
a = ("A","B",4,"C")
x,y,z = "A","b","C"
print(x)
print(y)
print(z)
b = ("A","B",4,"C")
# x,y,z = b # error => too many values to unpack (expected 3, got 4)
x,y,_,z = b
print(x)
print(y)
print(z)