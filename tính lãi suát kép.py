von = 100000000
lai_suat = 0.07 
nam = 10
print(f"Đầu tư {von:,} VND với lãi suất {lai_suat*100:.0f}% trong {nam} năm.")
for i in range(1, nam + 1):
    von = von * (1 + lai_suat)
    print(f"Năm {i:>2}: {von:,.0f} VND") 
print(f"\nSau {nam} năm: {von:,.0f} VND")