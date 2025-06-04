#!/usr/bin/env python3
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5 import uic
import requests


class RSAMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        """Initialize the user interface"""
        print("Initializing RSA GUI application...")
        
        # Get the absolute path to the UI file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(current_dir, 'ui', 'rsa.ui')
        print(f"Loading UI file: {ui_file}")
        
        try:
            # Load UI file with absolute path
            uic.loadUi(ui_file, self)
            print("UI file loaded successfully!")
        except Exception as e:
            print(f"Error loading UI file: {e}")
            QMessageBox.critical(None, "Error", f"Failed to load UI file: {e}")
            sys.exit(1)
        
        # Set window properties
        self.setWindowTitle("RSA Encryption Tool")
        self.resize(800, 700)
        
        # Window management settings to ensure visibility
        self.setWindowFlags(Qt.Window)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowState(Qt.WindowNoState)
        
        print("UI initialization completed successfully!")

    def connect_signals(self):
        """Connect button signals to their respective slots"""
        print("Connecting button signals...")
        try:
            self.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
            self.btn_encrypt.clicked.connect(self.call_api_encrypt)
            self.btn_decrypt.clicked.connect(self.call_api_decrypt)
            self.btn_sign.clicked.connect(self.call_api_sign)
            self.btn_verify.clicked.connect(self.call_api_verify)
            print("Button signals connected successfully!")
        except AttributeError as e:
            print(f"Error connecting buttons: {e}")
            QMessageBox.critical(self, "Error", f"Failed to connect button signals: {e}")

    def call_api_gen_keys(self):
        """Generate RSA keys via API"""
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                QMessageBox.information(self, "Success", data["message"])
            else:
                QMessageBox.warning(self, "Error", f"API Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Failed to connect to API: {e}")

    def call_api_encrypt(self):
        """Encrypt message via API"""
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        
        # Get plain text from the text area
        plain_text = self.txt_plain_text.toPlainText()
        if not plain_text.strip():
            QMessageBox.warning(self, "Warning", "Please enter text to encrypt.")
            return
        
        payload = {
            "message": plain_text,
            "key_type": "public"
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.txt_cipher_text.setText(data["encrypted_message"])
                QMessageBox.information(self, "Success", "Text encrypted successfully!")
            else:
                QMessageBox.warning(self, "Error", f"API Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Failed to connect to API: {e}")

    def call_api_decrypt(self):
        """Decrypt message via API"""
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        
        # Get cipher text from the text area
        cipher_text = self.txt_cipher_text.toPlainText()
        if not cipher_text.strip():
            QMessageBox.warning(self, "Warning", "Please enter cipher text to decrypt.")
            return
        
        payload = {
            "ciphertext": cipher_text,
            "key_type": "private"
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.txt_plain_text.setText(data["decrypted_message"])
                QMessageBox.information(self, "Success", "Text decrypted successfully!")
            else:
                QMessageBox.warning(self, "Error", f"API Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Failed to connect to API: {e}")

    def call_api_sign(self):
        """Sign message via API"""
        url = "http://127.0.0.1:5000/api/rsa/sign"
        
        # Get message to sign
        message = self.txt_info.toPlainText()
        if not message.strip():
            QMessageBox.warning(self, "Warning", "Please enter text to sign.")
            return
        
        payload = {
            "message": message,
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.txt_sign.setText(data["signature"])
                QMessageBox.information(self, "Success", "Message signed successfully!")
            else:
                QMessageBox.warning(self, "Error", f"API Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Failed to connect to API: {e}")

    def call_api_verify(self):
        """Verify signature via API"""
        url = "http://127.0.0.1:5000/api/rsa/verify"
        
        # Get message and signature
        message = self.txt_info.toPlainText()
        signature = self.txt_sign.toPlainText()
        
        if not message.strip() or not signature.strip():
            QMessageBox.warning(self, "Warning", "Please enter both message and signature.")
            return
        
        payload = {
            "message": message,
            "signature": signature
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data["is_verified"]:
                    QMessageBox.information(self, "Verification Result", "Signature is VALID!")
                else:
                    QMessageBox.warning(self, "Verification Result", "Signature is INVALID!")
            else:
                QMessageBox.warning(self, "Error", f"API Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Failed to connect to API: {e}")

    def showEvent(self, event):
        """Override showEvent to ensure window appears correctly"""
        super().showEvent(event)
        self.raise_()
        self.activateWindow()


def main():
    """Main application entry point"""
    print("Starting RSA GUI application...")
    
    # Create QApplication
    app = QApplication(sys.argv)
    print("QApplication created successfully.")
    
    try:
        # Create main window
        window = RSAMainWindow()
        print("Main window created successfully.")
        
        # Show window
        window.show()
        print("Window displayed successfully.")
        
        # Force window to front
        window.raise_()
        window.activateWindow()
        
        print("Starting event loop...")
        # Start event loop
        sys.exit(app.exec_())
        
    except Exception as e:
        print(f"Error starting application: {e}")
        import traceback
        traceback.print_exc()
        QMessageBox.critical(None, "Application Error", f"Failed to start application: {e}")


if __name__ == "__main__":
    main()
