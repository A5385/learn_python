# --------------------------------------------
# ------------ Dictionary Methods ------------
# --------------------------------------------
# [1] clear()
# [2] update()
# [3] copy()
# [4] keys() values()
# [5] setdefault()
# [6] popitem()
# [7] items()
# [8] fromkeys()
# --------------------------------------------

# [1] clear()
user = {"name": "Ahmed"}
print(user)
user.clear()
print(user)

#############################################################
print("#" * 60)
#############################################################
# [2] update()
member = {"name": "Osama"}
member["age"] = 40
member.update({"country": "Egypt"})
print(member)

#############################################################
print("#" * 60)
#############################################################
# [3] copy()
main = {"name": "Osama"}
b = main.copy()
print(b)
main.update({"skill": "Fighting"})
print(main)
print(b)

#############################################################
print("#" * 60)
#############################################################
# [4] keys() values()
print(main.keys())
print(main.values())

#############################################################
print("#" * 60)
#############################################################
# [5] setdefault()

user = {"name": "Osama"}
print(user)
print(user.setdefault("name", "Ahmed"))
print(user)
print(user.setdefault("age"))
print(user)
print(user.setdefault("age", 40))
print(user)

#############################################################
print("#" * 60)
#############################################################
# [6] popitem()

member = {"name": "Osama", "Skill": "PS5"}
print(member)
member.update({"age": 49})
print(member.popitem())

#############################################################
print("#" * 60)
#############################################################
# [7] items()

view = {"name": "Ahmed", "skill": "xBox"}
allItems = view.items()
print(view)
view["age"] = 40
print(allItems)

#############################################################
print("#" * 60)
#############################################################
# [8] fromkeys()
a = ("MyKeyOne", "MyKeyTwo", "MyKeysThree")
b = "X"
print(dict.fromkeys(a, b))
