from flask import Flask, jsonify, request
from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher

app = Flask(__name__)

rsa_cipher = RSACipher()
ecc_cipher = ECCCipher()

@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({"message": "RSA keys generated successfully"})

@app.route('/api/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    data = request.json
    message = data['message']
    key_type = data['key_type']
    private_key, public_key = rsa_cipher.load_keys()
    if key_type == 'public':
        key = public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({"error": "Siuuuuuuuuuuuuu"}), 400
    encrypt_message = rsa_cipher.encrypt(message, key)
    encrypt_hex = encrypt_message.hex()
    return jsonify({"encrypted_message": encrypt_hex})

@app.route('/api/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    data = request.json
    ciphertext_hex = data['ciphertext']
    key_type = data['key_type']
    private_key, public_key = rsa_cipher.load_keys()
    if key_type == 'public':
        key = public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({"error": "Invalid key type"}), 400
    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypt_message = rsa_cipher.decrypt(ciphertext, key)
    return jsonify({"decrypted_message": decrypt_message})

@app.route('/api/rsa/sign', methods=['POST'])
def rsa_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = rsa_cipher.load_keys()
    signature = rsa_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({"signature": signature_hex})

@app.route('/api/rsa/verify', methods=['POST'])
def rsa_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = rsa_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = rsa_cipher.verify(message, signature, public_key)
    return jsonify({"is_verified": is_verified})

# ECC cipher Algorithm
@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({"message": "ECC keys generated successfully"})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({"signature": signature_hex})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    _, public_key = ecc_cipher.load_keys()  # Fix: public_key là thứ 2
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({"is_verified": is_verified})


#main
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000 )
