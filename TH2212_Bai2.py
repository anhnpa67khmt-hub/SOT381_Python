a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
maxx = a
if b > maxx:
    maxx = b
if c > maxx:
    maxx= c
minn = a
if b < minn:
    minn = b
if c < minn:
    minn = c
print(f"Giá trị lớn nhất là: {maxx}")
print(f"Giá trị nhỏ nhất là: {minn}")