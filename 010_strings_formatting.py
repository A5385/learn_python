# ------------------------------------
# --- Strings Formatting - Old Way ---
# ------------------------------------

name = "Ahmed"
age = 40
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and my Age is: " + age) # type Error

print("My Name is: %s" % "Ahmed")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name,age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name,age,rank))

# %s => String
# %d => Number
# %f => Float

n = "Ahmed"
l = "Python"
y = 10

print("My name is %s, Iam %s Developer with %d years exp" %(n,l,y))

# Control Floating Point Number
myNumber = 10
print("My Number is: %d" % myNumber)
print("My Number is: %.2f" % myNumber)

# Truncate String
myLongString = "Hello Peoples of Elzero web school i love you all"
print("Message is %s" % myLongString)
print("Message is %.5s" % myLongString)



# ------------------------------------
# --- Strings Formatting - New Way ---
# ------------------------------------

name = "Ahmed"
age = 40
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and my Age is: " + age) # type Error

print("My Name is: {}".format("Ahmed"))
print("My Name is: {}".format(name))
print("My Name is: {} and My Age is: {}".format(name,age))
print("My Name is: {:s} and My Age is: {:d} and My Rank is: {:f}".format(name,age,rank))

# {:s} => String
# {:d} => Number
# {:f} => Float

n = "Ahmed"
l = "Python"
y = 10

print("My name is {}, Iam {} Developer with {:d} years exp".format(n,l,y))

# # Control Floating Point Number
myNumber = 10
print("My Number is: {:d}".format(myNumber))
print("My Number is: {:f}".format(myNumber))
print("My Number is: {:.2f}".format(myNumber))

# # Truncate String
myLongString = "Hello Peoples of Elzero web school i love you all"
print("Message is {}".format(myLongString))
print("Message is {:.5s}".format(myLongString))
print("Message is {:.13s}".format(myLongString))

# Format Money

myMoney = 500162350198
print("My Money in Bank is: {:d}".format(myMoney))
print("My Money in Bank is: {:_d}".format(myMoney))
print("My Money in Bank is: {:,d}".format(myMoney))
# print("My Money in Bank is: {:&d}".format(myMoney)) # error not all symbol valid to use

# ReArrange Items

a,b,c = "One","Two","Three"
print("Hello {} {} {}".format(a,b,c)) # Hello One Two Three
print("Hello {1} {2} {0}".format(a,b,c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a,b,c))  # Hello Three One Two

x,y,z = 10,20,30
print("Hello {} {} {}".format(x,y,z)) 
print("Hello {1:d} {2:d} {0:d}".format(x,y,z)) 
print("Hello {2:f} {0:f} {1:f}".format(x,y,z)) 
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x,y,z)) 

# Format in Version 3.6+

myName = "Ahmed"
myAge = 40

print(f"My Name is: {myName} and My Age is : {myAge}")
print(f"My Name is: {myName} and My Age is : {myAge:f}")
print(f"My Name is: {myName} and My Age is : {myAge:.2f}")
