def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
input_tuple = eval(input("Nhập một tuple cách nhau bởi dấu phẩy: "))
first, last = truy_cap_phan_tu(input_tuple)
print("Phần từ đầu tiên là : ", first)
print("Phần từ cuối cùng là : ", last)
