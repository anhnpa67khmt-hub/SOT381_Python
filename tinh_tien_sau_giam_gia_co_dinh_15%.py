MUC_GIAM_GIA_PHAN_TRAM = 15.0
HE_SO_THANH_TOAN = 1 - (MUC_GIAM_GIA_PHAN_TRAM / 100) 
gia_tri_don_hang = float(input("Mời nhập giá trị đơn hàng (VNĐ): "))
tien_duoc_giam = gia_tri_don_hang * (MUC_GIAM_GIA_PHAN_TRAM / 100)
tien_phai_tra = gia_tri_don_hang * HE_SO_THANH_TOAN
print("---------------------------------------")
print(f"Giá trị đơn hàng gốc: {gia_tri_don_hang:,.0f} VNĐ")
print(f"Mức giảm giá cố định: {MUC_GIAM_GIA_PHAN_TRAM:.0f}%")
print("---------------------------------------")
print(f"Số tiền được giảm là: {tien_duoc_giam:,.0f} VNĐ")
print(f"Số tiền khách hàng phải thanh toán là: {tien_phai_tra:,.0f} VNĐ")