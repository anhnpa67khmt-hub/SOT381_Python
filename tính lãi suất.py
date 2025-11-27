so_tien_dau_tu_ban_dau = 100000000  
lai_suat_nam = 0.07                 
so_nam_dau_tu = 10                  
so_tien_hien_tai = so_tien_dau_tu_ban_dau
print(f"--- Tính lãi suất kép (7%) sau {so_nam_dau_tu} năm ---")
print(f"Số tiền ban đầu: {so_tien_hien_tai:,.0f} VND\n")
for i in range(so_nam_dau_tu):
    tien_lai = so_tien_hien_tai * lai_suat_nam
    so_tien_hien_tai = so_tien_hien_tai + tien_lai
    nam_thu = i + 1
    print(f"Cuối năm {nam_thu:>2}: Số tiền có được: {so_tien_hien_tai:,.0f} VND (Lãi: {tien_lai:,.0f} VND)")
print("\n--- Hoàn thành ---")