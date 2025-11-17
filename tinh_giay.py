gio = int(input("Mời nhập số giờ: "))
phut = int(input("Mời nhập số phút: "))
giay = int(input("Mời nhập số giây: "))
GIO_SANG_GIAY = 3600
PHUT_SANG_GIAY = 60
tong_so_giay = (gio * GIO_SANG_GIAY) + \
               (phut * PHUT_SANG_GIAY) + \
               giay
print("---------------------------------------")
print(f"Thời gian đã nhập: {gio} giờ, {phut} phút, {giay} giây")
print("Tổng số giây tương ứng là:", tong_so_giay, "giây.")