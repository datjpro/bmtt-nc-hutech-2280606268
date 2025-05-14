def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập danh sách các số, các nhau bằng dấU phẩy: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
print("Danh sách: ",numbers)
print("Tuple từ danh sách:",my_tuple)