a = int(input("Mời nhập số nguyên a (số bị chia): "))
b = int(input("Mời nhập số nguyên b (số chia): "))
if b == 0:
    print("---------------------------------------")
    print("LỖI: Không thể chia cho 0!")
else:
    phan_nguyen = a // b
    phan_du = a % b
    print("---------------------------------------")
    print(f"Phép chia {a} cho {b}:")
    print("Phần nguyên của phép chia là:", phan_nguyen)
    print("Phần dư của phép chia là:", phan_du)