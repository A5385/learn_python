# --------------------------------------------------------------------------
# ------------- Control Flow - Make Decisions - if, elif, else -------------
# --------------------------------------------------------------------------
sep = "#" * 60

uName = "Ahmed"
uCountry = "Kuwait"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt":
    print(f"Hello {uName} because you are from {uCountry}")
    print(f'the course "{cName}" price is: ${cPrice - 80} ')

elif uCountry == "KSA":
    print(f"Hello {uName} because you are from {uCountry}")
    print(f'the course "{cName}" price is: ${cPrice - 70} ')

elif uCountry == "Kuwait":
    print(f"Hello {uName} because you are from {uCountry}")
    print(f'the course "{cName}" price is: ${cPrice - 50} ')

else:
    print(f"Hello {uName} because you are from {uCountry}")
    print(f'the course "{cName}" price is: ${cPrice - 30} ')


###############################################################
print(sep)  ###################################################
###############################################################
