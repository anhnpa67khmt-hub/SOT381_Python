try:
    n = int(input("Nhập vị trí n trong dãy Fibonacci (n >= 1): "))
    if n <= 0:
        print("Vị trí phải là số nguyên dương.")
    elif n == 1:
        print("Số Fibonacci thứ 1 là: 0")
    elif n == 2:
        print("Số Fibonacci thứ 2 là: 1")
    else:
        a = 0
        b = 1
        for _ in range(2, n):
            c = a + b  
            a = b      
            b = c
        print(f"Số Fibonacci thứ {n} là: {b}")
except ValueError:
    print("Đầu vào không hợp lệ.")