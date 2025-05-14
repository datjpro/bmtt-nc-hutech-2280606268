so_gio_lam = float(input("Nhap so  gio lam moi tuan"))
Luong_gio_lam = float(input("Nhap so luong gio lam "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0,so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * Luong_gio_lam + gio_tieu_chuan * Luong_gio_lam * 1.5
print(f"so tien thuc linh cua nhan vien {thuc_linh}")