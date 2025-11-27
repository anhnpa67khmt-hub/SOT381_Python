try:
    so_nguyen = int(input("Nhập một số nguyên: "))
    
    so_tam = abs(so_nguyen)  
    so_dao_nguoc = 0
    while so_tam > 0:
        chu_so = so_tam % 10
        so_dao_nguoc = so_dao_nguoc * 10 + chu_so
        so_tam //= 10
    if so_nguyen < 0:
        so_dao_nguoc *= -1
    print(f"Số đảo ngược của {so_nguyen} là: {so_dao_nguoc}")
except ValueError:
    print("Đầu vào không hợp lệ.")