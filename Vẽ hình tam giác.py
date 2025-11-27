try:
    chieu_cao = int(input("Nhập chiều cao tam giác (n): "))
    if chieu_cao <= 0:
        print("Chiều cao phải là số dương.")
    else:
        print("--- Hình Tam Giác ---")
        for i in range(1, chieu_cao + 1):
            print("*" * i)
except ValueError:
    print("Đầu vào không hợp lệ.")