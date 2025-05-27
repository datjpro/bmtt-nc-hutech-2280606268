from flask import Flask, render_template, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayfairCipher
from cipher.transposition.transposition_cipher import TranspositionCipher

app = Flask(__name__)

#router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

#router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

#router routes for vigenere cipher
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

#router routes for railfence cipher
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

#router routes for playfair cipher
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

#router routes for transposition cipher
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Vigenere Cipher API routes
@app.route("/api/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    try:
        data = request.get_json()
        text = data['text']
        key = data['key']
        vigenere = VigenereCipher()
        encrypted = vigenere.vigenere_encrypt(text, key)
        return jsonify({'success': True, 'result': encrypted})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route("/api/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    try:
        data = request.get_json()
        text = data['text']
        key = data['key']
        vigenere = VigenereCipher()
        decrypted = vigenere.vigenere_decrypt(text, key)
        return jsonify({'success': True, 'result': decrypted})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Rail Fence Cipher API routes
@app.route("/api/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    try:
        data = request.get_json()
        text = data['text']
        rails = int(data['rails'])
        railfence = RailFenceCipher()
        encrypted = railfence.rail_fence_encrypt(text, rails)
        return jsonify({'success': True, 'result': encrypted})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route("/api/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    try:
        data = request.get_json()
        text = data['text']
        rails = int(data['rails'])
        railfence = RailFenceCipher()
        decrypted = railfence.rail_fence_decrypt(text, rails)
        return jsonify({'success': True, 'result': decrypted})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Playfair Cipher API routes
@app.route("/api/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    try:
        data = request.get_json()
        text = data['text']
        key = data['key']
        playfair = PlayfairCipher()
        matrix = playfair.create_playfair_matrix(key)
        encrypted = playfair.playfair_encrypt(text, matrix)
        return jsonify({'success': True, 'result': encrypted})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route("/api/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    try:
        data = request.get_json()
        text = data['text']
        key = data['key']
        playfair = PlayfairCipher()
        matrix = playfair.create_playfair_matrix(key)
        decrypted = playfair.playfair_decrypt(text, matrix)
        return jsonify({'success': True, 'result': decrypted})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Transposition Cipher API routes
@app.route("/api/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    try:
        data = request.get_json()
        text = data['text']
        key = int(data['key'])
        transposition = TranspositionCipher()
        encrypted = transposition.encrypt(text, key)
        return jsonify({'success': True, 'result': encrypted})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route("/api/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    try:
        data = request.get_json()
        text = data['text']
        key = int(data['key'])
        transposition = TranspositionCipher()
        decrypted = transposition.decrypt(text, key)
        return jsonify({'success': True, 'result': decrypted})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)