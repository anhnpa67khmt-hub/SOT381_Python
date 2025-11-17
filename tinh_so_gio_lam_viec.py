so_gio_mot_ngay = float(input("Mời nhập số giờ làm việc mỗi ngày: "))
so_ngay_mot_thang = int(input("Mời nhập số ngày làm việc trong tháng: "))
tong_so_gio = so_gio_mot_ngay * so_ngay_mot_thang
print("---------------------------------------")
print(f"Số giờ làm việc mỗi ngày: {so_gio_mot_ngay} giờ")
print(f"Số ngày làm việc trong tháng: {so_ngay_mot_thang} ngày")
print("---------------------------------------")
print(f"Tổng số giờ làm việc trong tháng là: {tong_so_gio:,.1f} giờ")