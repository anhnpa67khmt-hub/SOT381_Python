PI = 3.14159
ban_kinh_r = float(input("Mời nhập bán kính hình tròn (r): "))
chu_vi = 2 * PI * ban_kinh_r
dien_tich = PI * (ban_kinh_r ** 2)
print("---------------------------------------")
print(f"Bán kính hình tròn đã nhập: {ban_kinh_r}")
print(f"Hằng số PI sử dụng: {PI}")
print("---------------------------------------")
# Định dạng kết quả lấy 3 chữ số thập phân
print(f"Chu vi hình tròn là: {chu_vi:,.3f}")
print(f"Diện tích hình tròn là: {dien_tich:,.3f}")