from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:

    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("1. Them sinh vien")
    print("2. Cap nhat sinh vien theo ID")
    print("3. Xoa sinh vien theo ID")
    print("4. Tim sinh vien theo ten")
    print("5. Sap xep theo diem TB")
    print("6. Sap xep theo ten")
    print("7. Hien thi danh sach")
    print("0. Thoat")

    key = int(input("Nhap lua chon: "))

    if key == 1:
        qlsv.nhapSinhVien()

    elif key == 2:
        ID = int(input("Nhap ID: "))
        qlsv.updateSinhVien(ID)

    elif key == 3:
        ID = int(input("Nhap ID can xoa: "))
        if qlsv.deleteById(ID):
            print("Da xoa sinh vien")
        else:
            print("Khong tim thay sinh vien")

    elif key == 4:
        name = input("Nhap ten can tim: ")
        result = qlsv.findByName(name)
        qlsv.showSinhVien(result)

    elif key == 5:
        qlsv.sortByDiemTB()
        qlsv.showSinhVien(qlsv.getListSinhVien())

    elif key == 6:
        qlsv.sortByName()
        qlsv.showSinhVien(qlsv.getListSinhVien())

    elif key == 7:
        qlsv.showSinhVien(qlsv.getListSinhVien())

    elif key == 0:
        break

    else:
        print("Lua chon khong hop le")
