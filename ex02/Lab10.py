def dao_nguoc_chieu(chuoi):
    return chuoi[::-1]
input_string = input("Moi nhap chuoi can dao nguoc ")
print("Chuoi dao nguoc la ",dao_nguoc_chieu(input_string))