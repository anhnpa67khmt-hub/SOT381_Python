chuoi = input("Nhập một số hoặc chuỗi để kiểm tra đối xứng: ")
chuoi_kiem_tra = chuoi.replace(" ", "").lower()
chuoi_dao_nguoc = chuoi_kiem_tra[::-1]
if chuoi_kiem_tra == chuoi_dao_nguoc:
    print(f"'{chuoi}' là đối xứng (Palindrome).")
else:
    print(f"'{chuoi}' không đối xứng.")