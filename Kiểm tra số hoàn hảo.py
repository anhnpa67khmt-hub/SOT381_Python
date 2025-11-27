try:
    n = int(input("Nhập một số để kiểm tra số hoàn hảo: "))
    if n <= 0:
        print("Vui lòng nhập số nguyên dương.")
    else:
        tong_uoc = 0
        for i in range(1, n):
            if n % i == 0:
                tong_uoc += i
        if tong_uoc == n:
            print(f"Số {n} là số hoàn hảo.")
        else:
            print(f"Số {n} không phải là số hoàn hảo (Tổng ước số: {tong_uoc}).")
except ValueError:
    print("Đầu vào không hợp lệ.")