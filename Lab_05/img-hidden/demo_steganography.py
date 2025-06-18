from PIL import Image, ImageDraw, ImageFont
import os

def create_sample_image():
    """Tạo một ảnh mẫu để test steganography"""
    # Tạo ảnh 300x200 pixels với nền xanh dương
    img = Image.new('RGB', (300, 200), color='lightblue')
    draw = ImageDraw.Draw(img)
    
    # Vẽ một hình chữ nhật
    draw.rectangle([50, 50, 250, 150], fill='white', outline='black', width=2)
    
    # Thêm text
    try:
        # Sử dụng font mặc định
        draw.text((100, 90), "HUTECH", fill='black')
        draw.text((80, 110), "Cybersecurity", fill='red')
    except:
        # Nếu không load được font, chỉ vẽ hình
        pass
    
    # Lưu ảnh
    img.save('sample_image.png')
    print("✅ Đã tạo ảnh mẫu: sample_image.png")
    return 'sample_image.png'

def encode_message_in_image(image_path, message):
    """Ẩn thông điệp trong ảnh"""
    img = Image.open(image_path)
    width, height = img.size
    
    # Chuyển message thành binary và thêm delimiter
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Dấu kết thúc
    
    data_index = 0
    pixels = list(img.getdata())
    new_pixels = []
    
    for pixel in pixels:
        if isinstance(pixel, int):  # Grayscale
            pixel = [pixel, pixel, pixel]
        else:
            pixel = list(pixel)
        
        # Modify RGB channels
        for channel in range(3):
            if data_index < len(binary_message):
                # Thay đổi bit cuối cùng
                pixel[channel] = (pixel[channel] & 0xFE) | int(binary_message[data_index])
                data_index += 1
        
        new_pixels.append(tuple(pixel[:3]))  # Chỉ lấy RGB
        
        if data_index >= len(binary_message):
            new_pixels.extend(pixels[len(new_pixels):])
            break
    
    # Tạo ảnh mới với dữ liệu đã được encode
    new_img = Image.new('RGB', (width, height))
    new_img.putdata(new_pixels)
    
    encoded_path = 'encoded_' + os.path.basename(image_path)
    new_img.save(encoded_path)
    print(f"✅ Đã ẩn thông điệp trong ảnh: {encoded_path}")
    return encoded_path

def decode_message_from_image(encoded_image_path):
    """Giải mã thông điệp từ ảnh"""
    img = Image.open(encoded_image_path)
    pixels = list(img.getdata())
    
    binary_message = ""
    
    for pixel in pixels:
        if isinstance(pixel, int):  # Grayscale
            pixel = [pixel, pixel, pixel]
        
        # Lấy bit cuối cùng từ mỗi channel
        for channel in range(3):
            binary_message += str(pixel[channel] & 1)
    
    # Chuyển binary thành text
    message = ""
    for i in range(0, len(binary_message), 8):
        if i + 8 <= len(binary_message):
            byte = binary_message[i:i+8]
            if byte == '11111110':  # Dấu kết thúc
                break
            char_code = int(byte, 2)
            if 32 <= char_code <= 126:  # Printable ASCII
                message += chr(char_code)
            elif char_code == 0:
                break
    
    return message

def main():
    print("🔐 STEGANOGRAPHY DEMO - HUTECH CYBERSECURITY LAB")
    print("=" * 60)
    
    # Tạo ảnh mẫu
    sample_image = create_sample_image()
    
    # Thông điệp cần ẩn
    secret_message = "Hello HUTECH! This is a secret message hidden in the image."
    print(f"📝 Thông điệp gốc: {secret_message}")
    
    # Encode thông điệp vào ảnh
    print("\n🔒 Đang ẩn thông điệp vào ảnh...")
    encoded_image = encode_message_in_image(sample_image, secret_message)
    
    # Decode thông điệp từ ảnh
    print("\n🔓 Đang giải mã thông điệp từ ảnh...")
    decoded_message = decode_message_from_image(encoded_image)
    print(f"📖 Thông điệp đã giải mã: {decoded_message}")
    
    # So sánh kết quả
    print("\n" + "=" * 60)
    if secret_message == decoded_message:
        print("✅ THÀNH CÔNG! Thông điệp đã được ẩn và giải mã chính xác.")
    else:
        print("❌ CÓ LỖI! Thông điệp giải mã không khớp với bản gốc.")
        print(f"Gốc: {repr(secret_message)}")
        print(f"Giải mã: {repr(decoded_message)}")
    
    print(f"\n📁 Các file đã tạo:")
    print(f"   - {sample_image} (ảnh gốc)")
    print(f"   - {encoded_image} (ảnh chứa thông điệp ẩn)")

if __name__ == "__main__":
    main()
