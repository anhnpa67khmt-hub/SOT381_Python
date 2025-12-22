def soLonNhat_vaNhoNhat(a, b, c):
    LN = a
    if b > LN:
        LN = b
    if c > LN:
        LN = c
    NN = a  
    if b < NN:
        NN = b
    if c < NN:
        NN = c
    return LN, NN 
m = float(input("Nhập số m: "))
n = float(input("Nhập số n: "))
k = float(input("Nhập số k: "))
numMax, numMin = soLonNhat_vaNhoNhat(m, n, k)
print(f"Số lớn nhất là {numMax}")
print(f"Số nhỏ nhất là {numMin}")