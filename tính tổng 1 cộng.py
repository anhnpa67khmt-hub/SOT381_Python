n = 5
tong_phan_so = 0
print(f"Tính tổng 1 + 1/2 + 1/3 + ... + 1/{n}:")
for i in range(1, n + 1):
    gia_tri = 1 / i 
    tong_phan_so = tong_phan_so + gia_tri 
    print(f"+ 1/{i} = {gia_tri:.3f} -> Tổng: {tong_phan_so:.3f}") 
print(f"Kết quả cuối cùng: {tong_phan_so:.3f}")