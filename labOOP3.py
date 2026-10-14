# Viết một chương trình Python cho phép tính diện tích và chu vi của các hình học
# như sau:
# 1. Tính diện tích và chu vi hình chữ nhật.
# 2. Tính diện tích và chu vi hình vuông.
# 3. Tính diện tích và chu vi hình tròn.
# 4. Tính diện tích và chu vi hình tam giác
# 5. Thoát.
# Chương trình sẽ được thể hiện theo dạng menu, cần tạo ra các class thể hiện các
# hình trên, mỗi class sẽ bao gồm một constructor cho phép truyền vào các tham số
# cần thiết, VD như hình chữ nhật sẽ bao gồm 2 tham số là chiều dài và chiều rộng.
# Mỗi một class sẽ bao gồm một method tính diện tích và một method tính chu vi.
# Hãy thực thi chương trình và in kết quả.
import math
class HinhChuNhat:
    def __init__(self, a, b):
        self.chieudai = a
        self.chieurong = b
    def dienTich(self):
        ketqua = self.chieudai * self.chieurong
        return ketqua
    def chuVi(self):
        ketqua = (self.chieudai + self.chieurong)*2
        return ketqua

class HinhVuong:
    def __init__(self, a):
        self.dodai = a
    def dienTich(self):
        ketqua = self.dodai * self.dodai
        return ketqua
    def chuVi(self):
        ketqua = self.dodai * 4
        return ketqua

class HinhTron:
    def __init__(self, r):
        self.bankinh = r
    def dienTich(self):
        pi = 3.14
        ketqua = pi * self.bankinh * self.bankinh
        return ketqua
    def chuVi(self):
        pi = 3.14
        ketqua = 2 * pi * self.bankinh
        return ketqua

class HinhTamGiac:
    def __init__(self, a, b, c):
        self.canh1 = a
        self.canh2 = b
        self.canh3 = c
    def kiemTraTamGiac(self):
        if self.canh1 + self.canh2 > self.canh3 and self.canh1 + self.canh3 > self.canh2 and self.canh2 + self.canh3 > self.canh1:
            return True
        else:
            return False
    def dienTich(self):
        if self.kiemTraTamGiac() == False:
            return "3 canh khong tao thanh tam giac"
        else:
            q = (self.canh1 + self.canh2 + self.canh3)/2
            ketqua = sqrt(q * (q-self.canh1)*(q-self.canh2)*(q-self.canh3))
            return ketqua
    def chuVi(self):
        if self.kiemTraTamGiac() == False:
            return "3 canh khong tao thanh tam giac"
        else:
            ketqua = self.canh1 + self.canh2 + self.canh3
            return ketqua
        
while True:
    print("Menu")
    print("1. Tinh dien tich va chu vi hinh chu nhat")
    print("2. Tinh dien tich va chu vi hinh vuong")
    print("3. Tinh dien tich va chu vi hinh tron")
    print("4. Tinh dien tich va chu vi hinh tam giac")
    print("5. Thoat")
    chon = int(input("Nhap lua chon: "))

    if chon == 1:
        a = float(input("Nhap chieu dai: "))
        b = float(input("Nhap chieu rong: "))
        Hinh1 = HinhChuNhat(a, b)
        print("dien tich la: ", Hinh1.dienTich())
        print("chu vi la: ", Hinh1.chuVi())
    elif chon == 2:
        a = float(input("Nhap canh: "))
        Hinh2 = HinhVuong(a)
        print("dien tich la: ", Hinh2.dienTich())
        print("chu vi la: ", Hinh2.chuVi())
    elif chon == 3:
        r = float(input("Nhap ban kinh: "))
        Hinh3 = HinhTron(r)
        print("dien tich la: ", Hinh3.dienTich())
        print("chu vi la: ", Hinh3.chuVi())
    elif chon == 4:
        a = float(input("Nhap canh thu nhat: "))
        b = float(input("Nhap canh thu hai: "))
        c = float(input("Nhap canh thu ba: "))
        Hinh4 = HinhTamGiac(a, b, c)
        print("dien tich la: ", Hinh4.dienTich())
        print("chu vi la: ", Hinh4.chuVi())
    elif chon == 5:
        print("Thoat chuong trinh")
        break
    else:
        print("lua chon khong hop le")



    
