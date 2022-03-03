x = int(input("X value: "))
y = int(input("Y value: "))
z = int(input("Z value: "))
x, y, z = abs(x), abs(y), abs(z)

if abs(z - x) == abs(z - y):
    print("Both are at the same distance")
elif x - z < y - z:
    print("X is the nearest one")
else:
    print("Y is the nearest one")