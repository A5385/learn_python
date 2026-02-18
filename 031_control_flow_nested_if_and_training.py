# ----------------------------------------------------
# ------------- Control Flow - Nested If -------------
# ----------------------------------------------------
sep = "#" * 60

uName = "Ahmed"
uCountry = "Egypt"
isStudent = "ds"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":

    if isStudent == "Yes":
        print(f"Hello {uName} because you are from {uCountry} and student")
        print(f'the course "{cName}" price is: ${cPrice - 90} ')
    else:
        print(f"Hello {uName} because you are from {uCountry}")
        print(f'the course "{cName}" price is: ${cPrice - 80} ')

elif uCountry == "Kuwait" or uCountry == "Bahrain":
    print(f"Hello {uName} because you are from {uCountry}")
    print(f'the course "{cName}" price is: ${cPrice - 50} ')

else:
    print(f"Hello {uName} because you are from {uCountry}")
    print(f'the course "{cName}" price is: ${cPrice - 30} ')


###############################################################
print(sep)  ###################################################
###############################################################
