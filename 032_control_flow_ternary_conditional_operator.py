# -----------------------------------------------------------------------
# ------------- Control Flow - Ternary Conditional Operator -------------
# -----------------------------------------------------------------------

country = "Egypt"

if country == "Egypt":
    print(f"The weather in {country} is 15")

elif country == "KSA":
    print(f"The weather in {country} is 30")

else:
    print("Country is not in the list")


# Short If

movieRate = 18
age = 16
if age < movieRate:
    print("Movie is not good for you")
else:
    print("Movie is good for you and have fun")

print(
    "Movie is not good for you"
    if age < movieRate
    else "Movie is good for you, and have fun"
)
