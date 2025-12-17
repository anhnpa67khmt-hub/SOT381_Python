try:
    n = int(input("Nhập vào số n: "))
    if n < 1:
        print("Vui lòng nhập số n >= 1.")
    else:
        tong = 0
        for i in range(1, n + 1):
            tong = tong + i
        print(f"Tổng các số tự nhiên từ 1 đến {n} là: {tong}") # Đã sửa lỗi: dùng print
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")