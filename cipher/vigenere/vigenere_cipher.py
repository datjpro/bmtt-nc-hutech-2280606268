class VigenereCipher:
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text, key):
        encrypt_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():  # Only encrypt alphabetic characters
                shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.islower():
                    encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                else:
                    encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                key_index += 1
                encrypt_text += encrypted_char  # Add encrypted character to the result
            else:
                encrypt_text += char  # Add non-alphabetic characters directly
        return encrypt_text

    def vigenere_decrypt(self, cipher_text, key):
        decrypt_text = ""
        key_index = 0
        for char in cipher_text:
            if char.isalpha():  # Only decrypt alphabetic characters
                shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.islower():
                    decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                else:
                    decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                key_index += 1
                decrypt_text += decrypted_char  # Add decrypted character to the result
            else:
                decrypt_text += char  # Add non-alphabetic characters directly
        return decrypt_text
