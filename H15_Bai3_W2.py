n = int(input("Nhập vào n (0 < n < 10): "))
if 0 < n < 10:
    giai_thua = 1
    i = 1
    while i <= n:
        giai_thua = giai_thua * i
        i = i + 1
    print(f"Kết quả {n}! là: {giai_thua}")
else:
    print("Số n không nằm trong khoảng cho phép.")