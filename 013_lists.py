# ---------------------------------------------------------
# ------------------------- Lists -------------------------
# ---------------------------------------------------------
# [1] List items are enclosed in square brackets
# [2] List are ordered, to use index to access item
# [3] List are mutable => add , delete, edit
# [4] List items is not unique
# [5] List can have different data types
# ---------------------------------------------------------

# [1] List items are enclosed in square brackets
myAwesomeList = []

# [2] List are ordered, to use index to access item
# [3] List are mutable => add , delete, edit
# [4] List items is not unique
myAwesomeList = ["One","Two","One"]
# [5] List can have different data types
myAwesomeList = ["One","Two","One",1,100.5,True]
# -------------

print(myAwesomeList) # Whole List
print(myAwesomeList[1]) # "One" => return string
print(myAwesomeList[-1]) # True => return string
print(myAwesomeList[-3]) # 1 => return string

print(myAwesomeList[1:4]) # ['Two', 'One', 1] => return list
print(myAwesomeList[:4]) # ['One', 'Two', 'One', 1] => return list
print(myAwesomeList[1:]) # ['Two', 'One', 1, 100.5, True] => return list

print(myAwesomeList[::1]) # ["One","Two","One",1,100.5,True] => return list
print(myAwesomeList[::2]) # ["One","One",100.5] => return list

myAwesomeList[1] = 2
myAwesomeList[-1] = False
myAwesomeList[0:2] = ["A","B","C"]
print(myAwesomeList)
myAwesomeList[0:3] = []
print(myAwesomeList)

