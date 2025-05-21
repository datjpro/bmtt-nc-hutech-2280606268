class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        # Tạo bảng rail rỗng với số dòng tương ứng
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1 nghĩa là di chuyển xuống, -1 nghĩa là di chuyển lên

        # Điền các ký tự vào các rail theo kiểu zigzag
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1  # Khi ở dòng đầu tiên, di chuyển xuống
            elif rail_index == num_rails - 1:
                direction = -1  # Khi ở dòng cuối cùng, di chuyển lên
            rail_index += direction  # Cập nhật chỉ số rail (dòng)

        # Đọc các ký tự theo chiều ngang để tạo ra chuỗi mã hóa
        encrypted_text = ''.join(''.join(rail) for rail in rails)
        return encrypted_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Tạo bảng rail rỗng với số dòng tương ứng
        rails = [['' for _ in range(len(cipher_text))] for _ in range(num_rails)]
        
        # Tạo bảng chỉ số để ghi nhận các vị trí đã được điền vào
        rail_index = 0
        direction = 1  # 1 nghĩa là di chuyển xuống, -1 nghĩa là di chuyển lên
        index = 0

        # Đặt các ký tự vào bảng theo hình zigzag
        for i in range(len(cipher_text)):
            rails[rail_index][i] = '*'  # Đánh dấu những vị trí sẽ được điền
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Điền các ký tự vào bảng
        for i in range(num_rails):
            for j in range(len(cipher_text)):
                if rails[i][j] == '*':  # Chỉ điền vào vị trí đánh dấu
                    rails[i][j] = cipher_text[index]
                    index += 1

        # Giải mã văn bản bằng cách đọc theo đường chéo
        decrypted_text = []
        rail_index = 0
        direction = 1
        for i in range(len(cipher_text)):
            decrypted_text.append(rails[rail_index][i])
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return ''.join(decrypted_text)


# Kiểm tra RailFenceCipher
rail_fence = RailFenceCipher()

plain_text = "HELLO"
num_rails = 3

# Mã hóa văn bản
encrypted_text = rail_fence.rail_fence_encrypt(plain_text, num_rails)
print(f"Encrypted: {encrypted_text}")

# Giải mã văn bản
decrypted_text = rail_fence.rail_fence_decrypt(encrypted_text, num_rails)
print(f"Decrypted: {decrypted_text}")
