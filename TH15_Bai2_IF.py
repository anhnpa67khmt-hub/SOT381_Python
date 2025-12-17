try:
    N = int(input("Nhập vào một số tự nhiên N: "))
    if N % 2 == 0 and N % 3 == 0:
        print(f"Số {N} là số chẵn và chia hết cho 3.")
    else:
        print(f"Số {N} KHÔNG thỏa mãn điều kiện (phải là số chẵn và chia hết cho 3).")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")