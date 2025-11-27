diem_so = [8.5, 7.0, 9.2, 6.8, 5.5, 8.8]
print("--- Kết quả phân loại học sinh ---")
for diem in diem_so:
    if diem >= 8.0:
        xep_loai = "GIỎI"
    elif diem >= 6.5:
        xep_loai = "KHÁ"
    else:
        xep_loai = "TRUNG BÌNH"
    print(f"Điểm: {diem:<4} => Xếp loại: {xep_loai}")