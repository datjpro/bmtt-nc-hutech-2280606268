from cipher.vigenere import VigenereCipher
from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.railfence import RailFenceCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypt_message': encrypt_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypt_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'encrypt_message': decrypt_text})

# Khởi tạo đối tượng VigenereCipher
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']  # Không cần ép kiểu ở đây vì key có thể là chuỗi
    # Sử dụng đúng phương thức vigenere_encrypt
    encrypt_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypt_message': encrypt_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    # Giải mã bằng phương thức vigenere_decrypt
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypt_message': decrypted_text})


railfence_cipher = RailFenceCipher()
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    num_rails = int(data['num_rails'])
    encrypt_text = railfence_cipher.rail_fence_encrypt(plain_text, num_rails)
    return jsonify({'encrypt_message': encrypt_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    num_rails = int(data['num_rails'])
    decrypt_text = railfence_cipher.rail_fence_decrypt(cipher_text, num_rails)
    return jsonify({'decrypt_message': decrypt_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
