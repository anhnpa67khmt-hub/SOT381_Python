try:
    so = int(input("Nhập một số nguyên: "))
    if so % 2 == 0:
        print(f"Số {so} là số chẵn.")
    else:
        print(f"Số {so} là số lẻ.")
except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")