# -----------------------------
# ------------ Dictionary ------------
# -----------------------------
# [1] Dict items enclosed in curly braces
# [2] Dict items are contains key : Value
# [3] Dict key need to be immutable => (Number, String, Tuple) list not allowed
# [4] Dict value can have any data types
# [5] Dict key need to be unique if you add 2 same keys the last one will use
# [6] Dict is not ordered you access its element with key
# [7] Two-Dimensional Dictionary
# -----------------------------

# [1] Dict items enclosed in curly braces
user = {}
print(user)

# [2] Dict items are contains key : Value
user = {
    "name": "Ahmed",
    "age": 50,
    "country": "Egypt",
}
print(user)

# [3] Dict key need to be immutable => (Number, String, Tuple) list not allowed
user = {
    "name": "Ahmed",
    "age": 50,
    "country": "Egypt",
    1: "test",
    # [2]:"test" # error => cannot use 'list' as a dict key (unhashable type: 'list')
    (2, 3): "test",
}
print(user)

# [4] Dict value can have any data types
user = {
    "name": "Ahmed",
    "age": 50,
    "country": "Egypt",
    "skills": ["Html", "Css", "JavaScript", "TypeScript"],
    "rating": 10.6,
}
print(user)

# [5] Dict key need to be unique if you add 2 same keys the last one will use
user = {
    "name": "Ahmed",
    "age": 50,
    "country": "Egypt",
    "skills": ["Html", "Css", "JavaScript", "TypeScript"],
    "rating": 10.6,
    "name": "Khaled",
}
print(user)

# [6] Dict is not ordered you access its element with key
user = {
    "name": "Ahmed",
    "age": 50,
    "country": "Egypt",
    "skills": ["Html", "Css", "JavaScript", "TypeScript"],
    "rating": 10.6,
    "name": "Khaled",
}
print(user["name"])
print(user.get("country"))

print(user.keys())
print(user.values())


# [7] Two-Dimensional Dictionary
languages = {
    "One": {"name": "Html", "progress": "80%"},
    "Two": {"name": "Css", "progress": "90%"},
    "Three": {"name": "Js", "progress": "90%"},
}
print(languages)
print(languages["One"])
print(languages["Three"]["progress"])
print(languages["Three"]["name"])
print(len(languages))
print(len(languages["Two"]))

# [8] create dictionary from variables

frameworkOne = {"name": "Angular", "progress": "80%"}
frameworkTwo = {"name": "ReactJs", "progress": "90%"}
frameworkThree = {"name": "NextJs", "progress": "80%"}

allFramework = {
    "One": frameworkOne,
    "Two": frameworkTwo,
    "Three": frameworkThree,
}

print(allFramework)
