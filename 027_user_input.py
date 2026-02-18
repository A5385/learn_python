# ---------------------------------------------
# ------------- User Input -------------
# ---------------------------------------------

sep = "#" * 60

fName = input("What's your first name?")
mName = input("What's your middle name?")
lName = input("What's your last name?")

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Hello {fName} {mName:.2s} {lName}, Happy to see you !")
###############################################################
print(sep)  ###################################################
###############################################################
