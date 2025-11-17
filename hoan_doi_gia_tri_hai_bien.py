a = int(input("Nhập giá trị của a: "))
b = int(input("Nhập giá trị của b: "))
print("--- Giá trị TRƯỚC khi hoán đổi ---")
print("a =", a)
print("b =", b)
a = a + b
b = a - b
a = a - b
print("--- Giá trị SAU khi hoán đổi ---")
print("a =", a)
print("b =", b)