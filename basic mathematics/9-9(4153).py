while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    elif x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
        print("right")
    else:
        print("wrong")


# 식이 쉬우면 고생할게 없음