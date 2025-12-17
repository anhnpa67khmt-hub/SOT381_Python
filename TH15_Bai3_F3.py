n = int(input("Nhập vào số n: "))
tong = 0
for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        tong = tong + i
print("Tổng các số chia hết cho 2 và 3 trong khoảng 1 đến", n, "là:", tong)