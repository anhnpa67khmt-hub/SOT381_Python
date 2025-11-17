tien_gui = float(input("Mời nhập số tiền gửi (VNĐ): "))
lai_suat_phan_tram = float(input("Mời nhập lãi suất (%/năm): "))
so_thang = int(input("Mời nhập số tháng gửi: "))
lai_suat_thap_phan = lai_suat_phan_tram / 100
tien_lai = (tien_gui * lai_suat_thap_phan * so_thang) / 12
print("---------------------------------------")
print("Tóm tắt thông tin:")
print("Tiền gửi gốc:", f"{tien_gui:,.0f}", "VNĐ") 
print("Lãi suất/năm:", lai_suat_phan_tram, "%")
print("Số tháng gửi:", so_thang, "tháng")
print("---------------------------------------")
print("Tổng tiền lãi nhận được là:", f"{tien_lai:,.2f}", "VNĐ")
tong_tien = tien_gui + tien_lai
print("Tổng số tiền cả gốc và lãi là:", f"{tong_tien:,.2f}", "VNĐ")