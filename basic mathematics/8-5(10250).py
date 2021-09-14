num= int(input())
for i in range(num):
    h, w, n = map(int, input().split())
    room_num = n // h # 반올림 하면 호텔 방 호수
    hotel_floor = n % h  # 호텔의 층 수
    if hotel_floor == 0:
        print((h * 100) + room_num)
    else:
        print((hotel_floor * 100) + (room_num + 1))

