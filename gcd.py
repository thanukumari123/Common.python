a = 24
b = 36
while b:
    a, b = b, a % b
print(a)