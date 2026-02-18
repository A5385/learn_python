# ---------------------------------------------
# ------------- Boolean Operators -------------
# ---------------------------------------------
# [1] and
# [2] or
# [3] not
# ---------------------------------------------

# [1] and
age = 36
country = "Egypt"
rank = 10
print(age > 16)
print(country == "Egypt")

print(age > 16 and country == "Egypt" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False

print("-" * 80)
# [2] or
print(age > 40 or country == "KSA" or rank > 20)  # False
print(age > 40 or country == "Egypt" or rank > 20)  # True

print("-" * 80)
# [3] not
print(age > 16)  # True
print(not age > 16)  # Not True  = False
