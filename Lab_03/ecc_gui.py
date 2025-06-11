import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import requests


class ECCApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load UI file directly
        uic.loadUi('ui/ecc.ui', self)
        
        # Connect buttons to functions
        self.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.btn_sign.clicked.connect(self.call_api_sign)
        self.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/ecc/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.setWindowTitle("ECC Key Generation")
                msg.exec_()
            else:
                self.show_error("Error while calling ECC generate keys API")
        except requests.exceptions.RequestException as e:
            self.show_error(f"Connection Error: {e}")

    def call_api_sign(self):
        # Get message from text area (textEdit from UI)
        message = self.textEdit.toPlainText().strip()
        
        if not message:
            self.show_warning("Please enter a message to sign!")
            return
            
        url = "http://127.0.0.1:5000/api/ecc/sign"
        payload = {
            "message": message
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Display signature in textEdit_2
                self.textEdit_2.setText(data["signature"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Message signed successfully!")
                msg.setWindowTitle("ECC Digital Signature")
                msg.exec_()
            else:
                self.show_error("Error while calling ECC sign API")
        except requests.exceptions.RequestException as e:
            self.show_error(f"Connection Error: {e}")

    def call_api_verify(self):
        # Get message and signature from text areas
        message = self.textEdit.toPlainText().strip()
        signature = self.textEdit_2.toPlainText().strip()
        
        if not message:
            self.show_warning("Please enter a message to verify!")
            return
            
        if not signature:
            self.show_warning("Please enter a signature to verify!")
            return
            
        url = "http://127.0.0.1:5000/api/ecc/verify"
        payload = {
            "message": message,
            "signature": signature
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data["is_verified"]:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("✅ Signature verification SUCCESSFUL!\n\nThe signature is valid for this message.")
                    msg.setWindowTitle("ECC Signature Verification")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("❌ Signature verification FAILED!\n\nThe signature is invalid or the message has been tampered with.")
                    msg.setWindowTitle("ECC Signature Verification")
                    msg.exec_()
            else:
                self.show_error("Error while calling ECC verify API")
        except requests.exceptions.RequestException as e:
            self.show_error(f"Connection Error: {e}")

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()
        
    def show_warning(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Warning")
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ECCApp()
    window.show()
    sys.exit(app.exec_())