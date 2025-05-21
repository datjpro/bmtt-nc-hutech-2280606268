from SinhVien import SinhVien
class QuanLySinhVien:
    listSinhVien = []

    def generateID(seft):
        maxId =1 
        if (seft.soLuongSinhVien()>0):
            maxId = seft.listSinhVien[0]._id
            for sv in seft.listSinhVien:
                if(maxId < sv._id):
                    maxId =sv._id
            maxId = maxId+1
        return maxId
        
    def soLuongSinhVien(seft):
        return seft.listSinhVien.__len__()

    def nhapSinhVien(seft):
        svId = seft.generateID()
        name = input("Nhap ten sv: ")
        sex = input("Nhap gioi tinh sv: ")
        major = input("Nhap chuyen nganh sv: ")
        diemTB = float(input("Nhap diem trung binh sv: "))
        sv = SinhVien(svId,name,sex,major,diemTB)
        seft.xepLoaiHocLuc(sv)
        seft.listSinhVien.append(sv)

    def updateSinhVien(seft, ID):
        sv:SinhVien = seft.findByID(ID)
        if (sv != None):
            name = input("Nhap ten sv: ")
            sex = input("Nhap gioi tinh sv: ")
            major = input("Nhap chuyen nganh sv: ")
            diemTB = float(input("Nhap diem trung binh sv: ")) 
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            seft.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co id = {} khong ton tai" .format(ID))
        
    def sortByID(self):
        self.listSinhVien.sort(key=lambda sv: sv._id)
    def sortByName(self):
        self.listSinhVien.sort(key=lambda sv: sv._name.lower())
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda sv: sv._diemTB, reverse=True)
    def findByID(sefl, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None
    def findByName(self, keyword):
        result = []
        keyword = keyword.lower()
        for sv in self.listSinhVien:
            if keyword in sv._name.lower():
                result.append(sv)
        return result

    
    def deleteByID(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            print(f"Sinh viên với ID = {ID} đã được xóa.")
        else:
            print(f"Sinh viên với ID = {ID} không tồn tại.")

    def xepLoaiHocLuc(self, sv):
        # Ví dụ logic xếp loại học lực (bạn có thể chỉnh sửa theo tiêu chí riêng)
        if sv._diemTB >= 8.5:
            sv._hocLuc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Khá"
        elif sv._diemTB >= 5.0:
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8} "
            .format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if len(listSV) > 0:
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8} "
                    .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")

    
    def getListSinhVien(self):
        return self.listSinhVien

