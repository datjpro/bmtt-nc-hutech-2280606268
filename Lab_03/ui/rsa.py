from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.setWindowTitle("RSA SIUUUUUUUU!")
        
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Main layout
        main_layout = QVBoxLayout(self.centralwidget)
        main_layout.setSpacing(10)
        
        # Title
        title_label = QLabel("RSA Encryption & Digital Signature Tool")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50; margin: 10px;")
        main_layout.addWidget(title_label)
        
        # Generate Keys button
        self.btn_gen_keys = QPushButton("🔑 Generate RSA Keys")
        self.btn_gen_keys.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        main_layout.addWidget(self.btn_gen_keys)
        
        # Encryption Section
        encryption_group = QLabel("📝 ENCRYPTION / DECRYPTION")
        encryption_group.setStyleSheet("font-size: 16px; font-weight: bold; color: #34495e; margin-top: 20px;")
        main_layout.addWidget(encryption_group)
        
        # Plain text area
        plain_label = QLabel("Plain Text:")
        plain_label.setStyleSheet("font-weight: bold; color: #2c3e50;")
        main_layout.addWidget(plain_label)
        
        self.txt_plain_text = QTextEdit()
        self.txt_plain_text.setMaximumHeight(100)
        self.txt_plain_text.setPlaceholderText("Enter your message here...")
        self.txt_plain_text.setStyleSheet("""
            QTextEdit {
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                padding: 5px;
                font-size: 12px;
            }
            QTextEdit:focus {
                border-color: #3498db;
            }
        """)
        main_layout.addWidget(self.txt_plain_text)
        
        # Encrypt/Decrypt buttons
        encrypt_layout = QHBoxLayout()
        self.btn_encrypt = QPushButton("🔒 Encrypt")
        self.btn_decrypt = QPushButton("🔓 Decrypt")
        
        button_style = """
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 8px 16px;
                font-size: 12px;
                font-weight: bold;
                border-radius: 5px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """
        
        self.btn_encrypt.setStyleSheet(button_style)
        self.btn_decrypt.setStyleSheet(button_style.replace("#27ae60", "#e74c3c").replace("#229954", "#c0392b"))
        
        encrypt_layout.addWidget(self.btn_encrypt)
        encrypt_layout.addWidget(self.btn_decrypt)
        main_layout.addLayout(encrypt_layout)
        
        # Cipher text area
        cipher_label = QLabel("Cipher Text (Hex):")
        cipher_label.setStyleSheet("font-weight: bold; color: #2c3e50;")
        main_layout.addWidget(cipher_label)
        
        self.txt_cipher_text = QTextEdit()
        self.txt_cipher_text.setMaximumHeight(100)
        self.txt_cipher_text.setPlaceholderText("Encrypted data will appear here...")
        self.txt_cipher_text.setStyleSheet("""
            QTextEdit {
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                padding: 5px;
                font-size: 12px;
                background-color: #f8f9fa;
            }
            QTextEdit:focus {
                border-color: #3498db;
            }
        """)
        main_layout.addWidget(self.txt_cipher_text)
        
        # Digital Signature Section
        signature_group = QLabel("✍️ DIGITAL SIGNATURE")
        signature_group.setStyleSheet("font-size: 16px; font-weight: bold; color: #34495e; margin-top: 20px;")
        main_layout.addWidget(signature_group)
        
        # Info text for signing
        info_label = QLabel("Message to Sign/Verify:")
        info_label.setStyleSheet("font-weight: bold; color: #2c3e50;")
        main_layout.addWidget(info_label)
        
        self.txt_info = QTextEdit()
        self.txt_info.setMaximumHeight(80)
        self.txt_info.setPlaceholderText("Enter message to sign or verify...")
        self.txt_info.setStyleSheet("""
            QTextEdit {
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                padding: 5px;
                font-size: 12px;
            }
            QTextEdit:focus {
                border-color: #3498db;
            }
        """)
        main_layout.addWidget(self.txt_info)
        
        # Sign/Verify buttons
        sign_layout = QHBoxLayout()
        self.btn_sign = QPushButton("✍️ Sign Message")
        self.btn_verify = QPushButton("✅ Verify Signature")
        
        sign_button_style = """
            QPushButton {
                background-color: #9b59b6;
                color: white;
                border: none;
                padding: 8px 16px;
                font-size: 12px;
                font-weight: bold;
                border-radius: 5px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #8e44ad;
            }
        """
        
        self.btn_sign.setStyleSheet(sign_button_style)
        self.btn_verify.setStyleSheet(sign_button_style.replace("#9b59b6", "#f39c12").replace("#8e44ad", "#e67e22"))
        
        sign_layout.addWidget(self.btn_sign)
        sign_layout.addWidget(self.btn_verify)
        main_layout.addLayout(sign_layout)
        
        # Signature area
        signature_label = QLabel("Digital Signature (Hex):")
        signature_label.setStyleSheet("font-weight: bold; color: #2c3e50;")
        main_layout.addWidget(signature_label)
        
        self.txt_sign = QTextEdit()
        self.txt_sign.setMaximumHeight(80)
        self.txt_sign.setPlaceholderText("Digital signature will appear here...")
        self.txt_sign.setStyleSheet("""
            QTextEdit {
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                padding: 5px;
                font-size: 12px;
                background-color: #f8f9fa;
            }
            QTextEdit:focus {
                border-color: #3498db;
            }
        """)
        main_layout.addWidget(self.txt_sign)
        
        # Footer
        footer_label = QLabel("💡 Tip: Generate keys first, then you can encrypt/decrypt messages and create digital signatures")
        footer_label.setAlignment(Qt.AlignCenter)
        footer_label.setStyleSheet("color: #7f8c8d; font-style: italic; margin-top: 10px;")
        main_layout.addWidget(footer_label)
