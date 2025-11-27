so_luong = [15, 8, 22, 5, 12, 3]
ten_san_pham = ["Áo", "Quần", "Giày", "Túi", "Mũ", "Ví"]
print("--- Danh sách sản phẩm cần nhập thêm ---")
for i in range(len(so_luong)):
    ton_kho = so_luong[i]
    if ton_kho < 10:
        ten = ten_san_pham[i]
        print(f"- Sản phẩm: {ten}, Tồn kho: {ton_kho}")