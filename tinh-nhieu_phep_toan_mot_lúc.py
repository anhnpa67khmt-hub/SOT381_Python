a = float(input("Mời nhập số a: "))
b = float(input("Mời nhập số b: "))
if b == 0:
    print("---------------------------------------")
    print("LỖI: Không thể thực hiện phép chia (/, //, %) hoặc lũy thừa với b=0!")
else:
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong = a / b
    luy_thua = a ** b
    phan_nguyen = a // b
    phan_du = a % b
    print("---------------------------------------")
    print(f"Hai số đã nhập: a={a}, b={b}")
    print("---------------------------------------")
    print(f"1. Tổng (a + b)           = {tong:,.2f}")
    print(f"2. Hiệu (a - b)           = {hieu:,.2f}")
    print(f"3. Tích (a * b)           = {tich:,.2f}")
    print(f"4. Thương (a / b)         = {thuong:,.2f}")
    print(f"5. Lũy thừa (a ** b)      = {luy_thua:,.2f}")
    print(f"6. Phần nguyên (a // b)   = {phan_nguyen:,.0f}")
    print(f"7. Phần dư (a % b)        = {phan_du:,.2f}")
