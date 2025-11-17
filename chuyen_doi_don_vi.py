CM_TREN_METER = 100
MM_TREN_METER = 1000
so_met = float(input("Mời nhập số mét cần chuyển đổi: "))
so_centimet = so_met * CM_TREN_METER
so_milimet = so_met * MM_TREN_METER
print("---------------------------------------")
print(f"Số mét đã nhập: {so_met} m")
print("---------------------------------------")
print(f"Giá trị tương ứng theo Centimet là: {so_centimet:,.2f} cm")
print(f"Giá trị tương ứng theo Milimet là: {so_milimet:,.2f} mm")