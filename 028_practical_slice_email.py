# ---------------------------------------------
# ------------- Practical Slice Email -------------
# ---------------------------------------------
sep = "#" * 60

theName = input("What's your name?").strip().capitalize()
theEmail = input("What's your Email?").strip().lower()

pos = theEmail.index("@")

username = theEmail[:pos].capitalize()
website = theEmail[pos + 1 :]

print(f"Hello {theName} your email is {theEmail}")
print(f"Your username is {username} \nYour website is {website}")
