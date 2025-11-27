n = 10
tong_le = 0
print(f"Các số lẻ từ 1 đến {n} được cộng là:")
for i in range(1, n + 1, 2):
    tong_le = tong_le + i
    print(f"- {i}") 
print(f"\nTổng số lẻ: {tong_le}")