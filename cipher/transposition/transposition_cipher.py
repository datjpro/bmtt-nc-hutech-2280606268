class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text
    
    def decrypt(self, text, key):
        num_rows = (len(text) + key - 1) // key
        decrypted_chars = [''] * len(text)
        text_index = 0
        for col in range(key):
            position = col
            while position < len(text):
                if text_index < len(text):
                    decrypted_chars[position] = text[text_index]
                    text_index += 1
                position += key
        
        return ''.join(decrypted_chars)