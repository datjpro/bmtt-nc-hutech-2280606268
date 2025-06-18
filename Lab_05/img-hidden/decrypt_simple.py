import sys
import os

def binary_to_text(binary):
    """Chuyển đổi binary thành text"""
    text = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))
    return text

def decode_message_simple(data_file, delimiter='###END###'):
    """Giải mã thông điệp từ file dữ liệu"""
    try:
        with open(data_file, 'r') as f:
            lines = f.readlines()
        
        # Lấy các giá trị pixel (bỏ qua comment lines)
        pixel_values = []
        for line in lines:
            if not line.startswith('#') and line.strip():
                values = line.strip().split()
                for val in values:
                    try:
                        pixel_values.append(int(val))
                    except ValueError:
                        continue
        
        # Trích xuất LSB để tạo binary message
        binary_message = ''
        for pixel in pixel_values:
            lsb = pixel & 1  # Lấy bit cuối cùng
            binary_message += str(lsb)
        
        # Chuyển binary thành text
        decoded_text = binary_to_text(binary_message)
        
        # Tìm delimiter để lấy message thực
        delimiter_pos = decoded_text.find(delimiter)
        if delimiter_pos != -1:
            actual_message = decoded_text[:delimiter_pos]
            return actual_message
        else:
            # Nếu không tìm thấy delimiter, trả về 50 ký tự đầu
            return decoded_text[:50].rstrip('\x00')
            
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt_simple.py <encoded_data_file>")
        print("Example: python decrypt_simple.py image_data.txt")
        return
    
    data_file = sys.argv[1]
    
    if not os.path.exists(data_file):
        print(f"❌ File not found: {data_file}")
        return
    
    print(f"🔍 Decoding message from: {data_file}")
    
    decoded_message = decode_message_simple(data_file)
    
    print(f"📜 Decoded message: '{decoded_message}'")

if __name__ == "__main__":
    main()
