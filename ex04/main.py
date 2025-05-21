from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nChương trình quản lý sinh viên")
    print("               Menu              ")
    print("1. Thêm sinh viên")
    print("2. Cập nhật sinh viên theo ID")
    print("3. Xóa sinh viên theo ID")
    print("4. Tìm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo điểm trung bình")
    print("6. Sắp xếp sinh viên theo tên chuyên ngành")
    print("7. Hiển thị danh sách sinh viên")
    print("0. Thoát")
    print("             ec ec ec            ")

    choice = input("Chọn một số: ")

    if choice == "1":
        qlsv.nhapSinhVien()
    elif choice == "2":
        ID = int(input("Nhập ID sinh viên cần cập nhật: "))
        qlsv.updateSinhVien(ID)
    elif choice == "3":
        ID = int(input("Nhập ID sinh viên cần xóa: "))
        qlsv.deleteByID(ID)
    elif choice == "4":
        keyword = input("Nhập tên sinh viên cần tìm: ")
        found_students = qlsv.findByName(keyword)
        if found_students:
            qlsv.showSinhVien(found_students)
        else:
            print("Không tìm thấy sinh viên.")
    elif choice == "5":
        qlsv.sortByDiemTB()
        print("Danh sách sinh viên đã được sắp xếp theo điểm trung bình.")
        qlsv.showSinhVien(qlsv.listSinhVien)
    elif choice == "6":
        qlsv.sortByName()
        print("Danh sách sinh viên đã được sắp xếp theo tên chuyên ngành.")
        qlsv.showSinhVien(qlsv.listSinhVien)
    elif choice == "7":
        qlsv.showSinhVien(qlsv.listSinhVien)
    elif choice == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
