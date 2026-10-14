# Viết một chương trình cho phép định nghĩa lớp. Tạo ra một lớp Calculator thể
# hiện máy tính điện tử. Định nghĩa 4 method add(), minus(), devide(), multiple()
# cho phép thể hiện 4 phép tính cơ bản.
# Sau đó hãy định nghĩa method factorial() cho phép tính và in ra giai thừa của
# tham số.
# Tiếp theo hãy khởi tạo một đối tượng của lớp, rồi gọi 4 method của lớp để xem
# kết quả. Chú ý: Hai số được nhập vào từ bàn phím.
class Calculator:
    def __init__(self, a, b):
        self.so1 = a
        self.so2 = b
    def add(self):
        ketqua = self.so1 + self.so2
        return ketqua
    def minus(self):
        ketqua = self.so1 - self.so2
        return ketqua
    def multiple(self):
        ketqua = self.so1 * self.so2
        return ketqua
    def devide(self):
        if self.so2 == 0: 
            return "gia tri chia bi loi"
        else: 
            ketqua = self.so1/self.so2
        return ketqua
    def factorial(self, a):
        giaithua = 1
        for i in range(1, a+1):
            giaithua = giaithua * i
        return giaithua
c = int(input())
d = int(input())
Phep1 = Calculator(c, d)
print("phep cong la: ", Phep1.add())
print("phep tru la: ", Phep1.minus())
print("phep nhan la: ", Phep1.multiple())
print("phep chia la: ", Phep1.devide())
print("giai thua la: ", Phep1.factorial(c))

