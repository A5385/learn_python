# -----------------------------
# -------- Set Methods --------
# -----------------------------
# [1] clear()
# [2] union() / |
# [3] add()
# [4] copy()
# [5] remove()
# [6] discard()
# [7] pop()
# [8] update()
# [9] difference()
# [10] difference_update()
# [11] intersection()
# [12] intersection_update()
# [13] symmetric_difference()
# [14] symmetric_difference_update
# -----------------------------

# [1] clear()
a = {1,2,3}
a.clear()
print(a)

print("-" * 40) ############ Separator ############

# [2] union()
b = {"One","Two","Three"}
c = {1,2,3}
x = {"Zero","Cool"}
print(b|c|x)
print(b.union(c,x))

print("-" * 40) ############ Separator ############

# [3] add()
d = {1,2,3,4}
d.add(5)
d.add(6)
print(d)

print("-" * 40) ############ Separator ############

# [4] copy()
e={1,2,3,4}
f=e.copy()
print(e)
print(f)
e.add(6)
print(e)
print(f)

print("-" * 40) ############ Separator ############

# [5] remove()
g = {1,2,3,4}
g.remove(1)
print(g)
# g.remove(7) # Error => KeyError: 7
print(g)

print("-" * 40) ############ Separator ############

# [6] discard()
h= {1,2,3,4}
h.discard(1)
print(h)
h.discard(7) 
print(h)

print("-" * 40) ############ Separator ############

# [7] pop()
i = {"A",True,1,2,3,4,5}
print(i.pop()) # pop one element randomly

print("-" * 40) ############ Separator ############

# [8] update()
j={1,2,3}
k={1,"A","B",2}
j.update(["Html","Css"])
j.update(k)
print(j)

print("-" * 40) ############ Separator ############

# [9] difference()
k={1,2,3,4}
l={1,2,3,"Ahmed","Khaled"}
print(k)
print(k.difference(l))
print(k)

print("-" * 40) ############ Separator ############

# [10] difference_update()
m={1,2,3,4}
n={1,2,3,"Ahmed","Khaled"}
print(m)
m.difference_update(n)
print(m)

print("-" * 40) ############ Separator ############

# [11] intersection()
e={1,2,3,4,"X"}
f={"Ahmed","X",2}
print(e)
print(e.intersection(f))
print(e)

print("-" * 40) ############ Separator ############

# [12] intersection_update()
e={1,2,3,4,"X"}
f={"Ahmed","X",2}
print(e)
e.intersection_update(f)
print(e)

print("-" * 40) ############ Separator ############

# [13] symmetric_difference()
i = {1,2,3,4,5,"X"}
j = {"Ahmed","Khaled",1,2,4}
print(i)
print(i.symmetric_difference(j))
print(i)

print("-" * 40) ############ Separator ############

# [14] symmetric_difference_update
i = {1,2,3,4,5,"X"}
j = {"Ahmed","Khaled",1,2,4}
print(i)
i.symmetric_difference_update(j)
print(i)

print("-" * 40) ############ Separator ############

# [15] issuperset()
# if you have set a and b check every elements in set b is in original set a and this return boolean 
a = {1,2,3,4}
b = {1,2,3}
c = {1,2,3,4,5}
print(a.issuperset(b)) # True => all element in b is in a
print(a.issuperset(c)) # False => all element in c not in a 


print("-" * 40) ############ Separator ############

# [16] issubset()
# opposite to issuperset if you have set a and b check every element in original set a is in set b and return boolean
a = {1,2,3,4}
b = {1,2,3}
c = {1,2,3,4,5}
print(a.issubset(b)) # False => all element in a is not in b 
print(a.issubset(c)) # True => all element in a in c


print("-" * 40) ############ Separator ############

# [17] isdisjoint()
a = {1,2,3,4}
b = {1,2,3}
c = {5,6,7,8}

print(a.isdisjoint(b)) # False
print(a.isdisjoint(c)) # True

print("-" * 40) ############ Separator ############


