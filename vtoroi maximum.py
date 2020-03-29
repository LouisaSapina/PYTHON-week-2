n = int(input())
max1 = 0
max2 = 0

while n != 0:
    if max1 <= n and max2 != n:
        max2 = max1
        max1 = n
    elif max2 <= n:
        max2 = n
    n = int(input())
print(max2)