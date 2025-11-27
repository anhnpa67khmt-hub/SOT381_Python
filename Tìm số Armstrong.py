try:
    so_nguyen = input("Nhập một số để kiểm tra số Armstrong: ")
    n_chu_so = len(so_nguyen)
    tong_luy_thua = 0
    for chu_so_ky_tu in so_nguyen:
        chu_so = int(chu_so_ky_tu)
        tong_luy_thua += chu_so ** n_chu_so
    if tong_luy_thua == int(so_nguyen):
        print(f"Số {so_nguyen} là số Armstrong.")
    else:
        print(f"Số {so_nguyen} không phải là số Armstrong.")
except ValueError:
    print("Đầu vào không hợp lệ.")