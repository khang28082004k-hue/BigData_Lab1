# Viết một chương trình cho phép định nghĩa lớp. Tạo ra một lớp có tên là Person, bao
# gồm 3 thuộc tính là name, address và age. Định nghĩa 2 method của lớp này có tên là
# inputDetails() và displayDetails() để cho phép nhập các giá trị cho các thuộc tính, và hiển
# thị giá trị của các thuộc tính của lớp.
# Tiếp theo, hãy khai báo 2 đối tượng của lớp, rồi gọi các method của 2 đối tượng này để
# xem kết quả.

class Person:
    def __init__(self, name="", address="", age=0):
        self.ten = name
        self.diachi = address
        self.tuoi = age
    
    def inputDetails(self):
        self.ten = str(input("nhap tu ban phim ten: "))
        self.diachi = str(input("nhap dia chi tu ban phim: "))
        self.tuoi = int(input("nhap tuoi tu ban phim: "))
    def displayDetails(self):
        print("ten la: ", self.ten)
        print("dia chi la: ", self.diachi)
        print("tuoi la: ", self.tuoi)

Nguoi1 = Person()
Nguoi1.inputDetails()
Nguoi1.displayDetails()

Nguoi2 = Person()
Nguoi2.inputDetails()
Nguoi2.displayDetails()

