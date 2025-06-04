import rsa
import os
os.environ['QT_QPA_PLATFORM'] = "../platform"

class RSACipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        
    def generate_keys(self, key_size=2048):
        """Generate RSA key pair"""
        self.public_key, self.private_key = rsa.newkeys(key_size)
        self.save_keys()
        
    def save_keys(self):
        """Save keys to files"""
        if not os.path.exists('keys'):
            os.makedirs('keys')
            
        # Save private key
        with open('keys/private_key.pem', 'wb') as f:
            f.write(self.private_key.save_pkcs1())
            
        # Save public key
        with open('keys/public_key.pem', 'wb') as f:
            f.write(self.public_key.save_pkcs1())
            
    def load_keys(self):
        """Load keys from files"""
        try:
            with open('keys/private_key.pem', 'rb') as f:
                private_key = rsa.PrivateKey.load_pkcs1(f.read())
                
            with open('keys/public_key.pem', 'rb') as f:
                public_key = rsa.PublicKey.load_pkcs1(f.read())
                
            return private_key, public_key
        except FileNotFoundError:
            raise Exception("Keys not found. Please generate keys first.")
            
    def encrypt(self, message, key):
        """Encrypt message with RSA key"""
        message_bytes = message.encode('utf-8')
        encrypted = rsa.encrypt(message_bytes, key)
        return encrypted
        
    def decrypt(self, ciphertext, key):
        """Decrypt ciphertext with RSA key"""
        decrypted_bytes = rsa.decrypt(ciphertext, key)
        return decrypted_bytes.decode('utf-8')
        
    def sign(self, message, private_key):
        """Sign message with private key"""
        message_bytes = message.encode('utf-8')
        signature = rsa.sign(message_bytes, private_key, 'SHA-256')
        return signature
        
    def verify(self, message, signature, public_key):
        """Verify signature with public key"""
        try:
            message_bytes = message.encode('utf-8')
            rsa.verify(message_bytes, signature, public_key)
            return True
        except rsa.VerificationError:
            return False