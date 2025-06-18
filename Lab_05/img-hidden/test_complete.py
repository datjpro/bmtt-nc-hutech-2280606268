from PIL import Image
import os

def test_steganography():
    print("🔐 STEGANOGRAPHY TEST - HUTECH CYBERSECURITY LAB")
    print("=" * 60)
    
    # Test messages
    test_messages = [
        "Hello HUTECH!",
        "Cybersecurity Lab 2024",
        "Secret message 123",
        "tophamthanhdat"
    ]
    
    # Kiểm tra xem có ảnh test không
    if not os.path.exists("image.jpg"):
        print("❌ Không tìm thấy file image.jpg")
        return
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n🧪 Test {i}: '{message}'")
        print("-" * 40)
        
        # Encode
        try:
            img = Image.open("image.jpg")
            width, height = img.size
            
            # Chuyển message thành binary
            binary_message = ''.join(format(ord(char), '08b') for char in message)
            
            data_index = 0
            for row in range(height):
                for col in range(width):
                    pixel = list(img.getpixel((col, row)))
                    
                    for color_channel in range(3):
                        if data_index < len(binary_message):
                            pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                            data_index += 1
                    
                    img.putpixel((col, row), tuple(pixel))
                    
                    if data_index >= len(binary_message):
                        break
                
                if data_index >= len(binary_message):
                    break
            
            encoded_path = f"test_encode_{i}.png"
            img.save(encoded_path)
            print(f"✅ Encoded: {encoded_path}")
            
            # Decode
            encoded_img = Image.open(encoded_path)
            binary_data = ""
            
            for row in range(height):
                for col in range(width):
                    pixel = encoded_img.getpixel((col, row))
                    
                    for color_channel in range(3):
                        binary_data += format(pixel[color_channel], '08b')[-1]
            
            decoded_message = ""
            for j in range(0, len(binary_data), 8):
                if j + 8 <= len(binary_data):
                    char = chr(int(binary_data[j:j+8], 2))
                    if 32 <= ord(char) <= 126:
                        decoded_message += char
                    else:
                        break
            
            # Lấy chỉ phần message gốc
            if len(decoded_message) >= len(message):
                decoded_message = decoded_message[:len(message)]
            
            print(f"📤 Original: {message}")
            print(f"📥 Decoded:  {decoded_message}")
            
            if message == decoded_message:
                print("✅ SUCCESS!")
            else:
                print("❌ FAILED!")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print(f"\n" + "=" * 60)
    print("🎯 STEGANOGRAPHY TEST COMPLETED")
    print("=" * 60)

if __name__ == "__main__":
    test_steganography()
