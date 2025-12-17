try:
    a = int(input("Nhập độ dài cạnh thứ nhất (số nguyên): "))
    b = int(input("Nhập độ dài cạnh thứ hai (số nguyên): "))
    if a <= 0 or b <= 0:
        print("Lỗi: Độ dài các cạnh phải là số nguyên dương.")
    else:
        chu_vi = 2 * (a + b)
        dien_tich = a * b
        print(f"\n--- Kết Quả ---")
        print(f"Cạnh a: {a}")
        print(f"Cạnh b: {b}")
        print(f"Chu vi của hình chữ nhật là: {chu_vi}")
        print(f"Diện tích của hình chữ nhật là: {dien_tich}")
except ValueError:
    print("Lỗi: Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")