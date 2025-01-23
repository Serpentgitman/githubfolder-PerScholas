#Creating a mixed-type list
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    # 45 is of the data type <class 'int'>
    # 290578 is of the data type <class 'int'>
    # 1.02 is of the data type <class 'float'>
    # True is of the data type <class 'bool'>
    # My dog is on the bed. is of the data type <class 'str'>
    # 45 is of the data type <class 'str'>