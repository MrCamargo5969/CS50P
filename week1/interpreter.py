x = input("Expression: ").split(" ")
y = float(x[0])
z = float(x[2])
if x[1] == "+":
    print(y + z)
elif x[1] == "-":
    print(y - z)
elif x[1] == "*":
    print(y * z)
elif x[1] == "/":
    print(y / z)
else:
    print("This isn`t a count")
