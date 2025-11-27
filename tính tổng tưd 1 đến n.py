n = 10
tong = 0
print(f"Tính tổng từ 1 đến {n}:")
for i in range(1, n + 1):
    tong = tong + i
    print(f"Thêm {i} → Tổng: {tong}") 
print(f"Kết quả: 1 + 2 + ... + {n} = {tong}")