import sys
import os

def text_to_binary(text):
    """Chuyển đổi text thành binary"""
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    """Chuyển đổi binary thành text"""
    text = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))
    return text

def encode_message_simple(message, delimiter='###END###'):
    """Mã hóa thông điệp thành binary với delimiter"""
    full_message = message + delimiter
    binary_message = text_to_binary(full_message)
    return binary_message

def create_sample_data(filename, message):
    """Tạo file dữ liệu mẫu với thông điệp ẩn"""
    # Tạo dữ liệu giả lập như là pixel data
    binary_message = encode_message_simple(message)
    
    # Tạo fake pixel data (giả lập RGB values)
    fake_pixels = []
    msg_index = 0
    
    # Tạo 1000 pixel giả (mỗi pixel có 3 giá trị RGB)
    for i in range(1000):
        for channel in range(3):  # R, G, B
            if msg_index < len(binary_message):
                # LSB encoding: thay đổi bit cuối cùng
                base_value = 128  # Giá trị cơ sở
                if binary_message[msg_index] == '1':
                    pixel_value = base_value | 1  # Set LSB to 1
                else:
                    pixel_value = base_value & 0xFE  # Set LSB to 0
                msg_index += 1
            else:
                pixel_value = base_value
            
            fake_pixels.append(pixel_value)
    
    # Lưu data vào file
    with open(filename, 'w') as f:
        f.write("# Fake image data with hidden message\n")
        f.write("# Format: pixel_values (simulated RGB)\n")
        for i, pixel in enumerate(fake_pixels):
            f.write(f"{pixel}")
            if (i + 1) % 20 == 0:  # 20 values per line
                f.write("\n")
            else:
                f.write(" ")

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt_simple.py <message> <output_file>")
        print("Example: python encrypt_simple.py 'Hello World' image_data.txt")
        return
    
    message = sys.argv[1]
    output_file = sys.argv[2]
    
    print(f"🔐 Encoding message: '{message}'")
    print(f"📁 Output file: {output_file}")
    
    create_sample_data(output_file, message)
    
    print("✅ Message encoded successfully!")
    print("🔍 Use decrypt_simple.py to extract the hidden message")

if __name__ == "__main__":
    main()
