def soLonNhat(a, b, c):
    LN = a  
    if b > LN:
        LN = b
    if c > LN:
        LN = c
    return LN
def soNhoNhat(a, b, c):
    NN = a  
    if b < NN:
        NN = b
    if c < NN:
        NN = c
    return NN
m = float(input("Nhập số thứ nhất (m): "))
n = float(input("Nhập số thứ hai (n): "))
k = float(input("Nhập số thứ ba (k): "))
numMax = soLonNhat(m, n, k)
numMin = soNhoNhat(m, n, k)
print(f"Số lớn nhất là: {numMax}")
print(f"Số nhỏ nhất là: {numMin}")