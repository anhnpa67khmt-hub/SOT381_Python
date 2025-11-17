diem_toan = float(input("Mời nhập điểm môn Toán: "))
diem_ly = float(input("Mời nhập điểm môn Lý: "))
diem_hoa = float(input("Mời nhập điểm môn Hóa: "))
SO_MON_HOC = 3
tong_diem = diem_toan + diem_ly + diem_hoa
diem_trung_binh = tong_diem / SO_MON_HOC
print("---------------------------------------")
print(f"Điểm Toán: {diem_toan}")
print(f"Điểm Lý: {diem_ly}")
print(f"Điểm Hóa: {diem_hoa}")
print(f"Điểm trung bình của 3 môn là: {diem_trung_binh:,.2f}")
