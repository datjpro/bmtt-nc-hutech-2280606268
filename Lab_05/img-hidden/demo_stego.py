import os
import subprocess

def run_command(command):
    """Chạy command và hiển thị kết quả"""
    print(f"💻 Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")
    return result.returncode == 0

def print_separator():
    print("=" * 60)

def main():
    print_separator()
    print("🕵️ STEGANOGRAPHY DEMO - HUTECH CYBERSECURITY LAB")
    print("📝 Simple Text Hiding in Data Files")
    print_separator()
    
    # Test messages
    test_messages = [
        "Hello HUTECH!",
        "Cybersecurity Lab 2024",
        "This is a secret message",
        "BMTT-NC-HUTECH"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n🔐 TEST {i}: Encoding message")
        print(f"📝 Message: '{message}'")
        
        output_file = f"encoded_data_{i}.txt"
        
        # Encode message
        encode_cmd = f'python encrypt_simple.py "{message}" {output_file}'
        success = run_command(encode_cmd)
        
        if success and os.path.exists(output_file):
            print(f"✅ Message encoded to {output_file}")
            
            # Show file size
            file_size = os.path.getsize(output_file)
            print(f"📊 File size: {file_size} bytes")
            
            # Decode message
            print(f"\n🔍 Decoding message from {output_file}")
            decode_cmd = f"python decrypt_simple.py {output_file}"
            run_command(decode_cmd)
            
        else:
            print(f"❌ Failed to encode message {i}")
        
        print("-" * 40)
    
    print_separator()
    print("📋 GENERATED FILES:")
    for i in range(1, len(test_messages) + 1):
        filename = f"encoded_data_{i}.txt"
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            print(f"📁 {filename} ({size} bytes)")
    
    print_separator()
    print("🎯 STEGANOGRAPHY CONCEPTS DEMONSTRATED:")
    print("• LSB (Least Significant Bit) encoding")
    print("• Binary representation of text")
    print("• Message delimiter for extraction")
    print("• Data hiding in numeric sequences")
    print_separator()
    
    print("\n🚀 Manual Testing:")
    print("python encrypt_simple.py 'Your Message' output.txt")
    print("python decrypt_simple.py output.txt")

if __name__ == "__main__":
    main()
