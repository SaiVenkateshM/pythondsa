def someFunction():
    global x
    x = 500
    print("x inside function",x)
someFunction()
print("x outside function:",x)