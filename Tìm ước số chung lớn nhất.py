def tim_ucln(a, b):
    while b:
        a, b = b, a % b
    return a
try:
    so_a = int(input("Nhập số a: "))
    so_b = int(input("Nhập số b: "))
    ket_qua = tim_ucln(so_a, so_b)
    print(f"Ước số chung lớn nhất của {so_a} và {so_b} là: {ket_qua}")
except ValueError:
    print("Đầu vào không hợp lệ.")