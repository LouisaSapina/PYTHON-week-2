a = int(input())
b = int(input())
c = int(input())
if a > c or b > c:
    if a > b:
        print(a)
    else:
        print(b)
else:
    print(c)
    print()