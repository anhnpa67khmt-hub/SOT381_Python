quang_duong_km = float(input("Mời nhập quãng đường đã đi (km): "))
thoi_gian_gio = float(input("Mời nhập thời gian đã đi (giờ): "))
if thoi_gian_gio == 0:
    print("---------------------------------------")
    print("LỖI: Thời gian không thể bằng 0 để tính vận tốc!")
else:
    van_toc_km_h = quang_duong_km / thoi_gian_gio
    print("---------------------------------------")
    print(f"Quãng đường đã nhập: {quang_duong_km} km")
    print(f"Thời gian đã nhập: {thoi_gian_gio} giờ")
    print(f"Vận tốc tương ứng là: {van_toc_km_h:,.2f} km/h")