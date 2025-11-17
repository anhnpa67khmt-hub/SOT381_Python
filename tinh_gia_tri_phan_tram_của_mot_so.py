so_x = float(input("Mời nhập số X gốc: "))
phan_tram_p = float(input("Mời nhập phần trăm P cần tính: "))
p_thap_phan = phan_tram_p / 100
ket_qua = so_x * p_thap_phan
print("---------------------------------------")
print(f"Bạn muốn tính {phan_tram_p}% của số {so_x}")
print("Giá trị tương ứng là:")
print(f"Kết quả = {ket_qua:,.2f}") 