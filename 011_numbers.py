# ------------------------------------------------
# ------------------- Numbers -------------------
# ------------------------------------------------
# Numbers Types => Integer - Float - Complex
# [1] You can convert from int to float or complex
# [2] You can Convert from float to int or complex
# [3] You cannot convert complex to any type
# ------------------------------------------------

# Integer
print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# Float
print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# Complex
myComplexNumber = 5+6j
print(type(myComplexNumber))
print("Real Part is: {}".format(myComplexNumber.real))
print("Imaginary Part is: {}".format(myComplexNumber.imag))


# [1] You can convert from int to float or complex

print(100)
print(float(100))
print(complex(100))

# [2] You can Convert from float to int or complex
print(10.50)
print(int(10.50))
print(complex(10.50))

# [3] You cannot convert complex to any type
print(10+9j)
print(int(10+9j))
print(float(10+9j))