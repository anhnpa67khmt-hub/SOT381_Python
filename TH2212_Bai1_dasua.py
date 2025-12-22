while True:
    w=float(input(" nhap do dai canh: "))
    h=float(input(" nhap do rong canh: "))
    if w>=0 and w<=100:
       break
    else:
        print(f"nhap da sai")
chu_vi= (w + h) * 2
dien_tich= w * h
print(f"Chu vi: {chu_vi:.2f}")
print(f"Diện tích: {dien_tich:.2f}")