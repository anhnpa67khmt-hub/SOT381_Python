key = ""

while key != "Y" and key != "y":
    key = input("Nhập vào chữ 'Y' hoặc 'y': ")
    if key != "Y" and key != "y":
        print("Sai rồi, vui lòng nhập lại!")
print("Login success!")