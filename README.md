# 🔐 Bảo Mật Thông Tin Nâng Cao - HUTECH

**Sinh viên:** Tô Phạm Thành Đạt  
**MSSV:** 2280606268  
**Môn học:** Bảo Mật Thông Tin Nâng Cao

## 📋 Mô tả dự án

Ứng dụng web hiện đại cho việc mã hóa và giải mã văn bản sử dụng các thuật toán mật mã cổ điển và hiện đại. Giao diện đẹp mắt với hiệu ứng glass morphism và animations mượt mà.

## ✨ Tính năng chính

### 🔢 Thuật toán được hỗ trợ:

- **Caesar Cipher** - Mã hóa dịch chuyển ký tự
- **Vigenère Cipher** - Mã hóa đa bảng chữ cái
- **Rail Fence Cipher** - Mã hóa hàng rào
- **Playfair Cipher** - Mã hóa ma trận 5x5
- **Transposition Cipher** - Mã hóa chuyển vị
- **RSA** - Mã hóa bất đối xứng (dự kiến)

### 🎨 Giao diện:

- **Modern UI/UX** với glass morphism design
- **Responsive** - tương thích mọi thiết bị
- **Dark theme** với gradient background
- **Smooth animations** và hover effects
- **Interactive cards** cho từng thuật toán

## 🛠 Công nghệ sử dụng

### Backend:

- **Python 3.x**
- **Flask** - Web framework
- **RESTful API** design

### Frontend:

- **HTML5** + **CSS3** + **JavaScript**
- **Google Fonts** (Inter)
- **Font Awesome** icons
- **CSS Animations** & **Keyframes**

## 📂 Cấu trúc thư mục

```
bmtt-nc-hutech-2280606268/
├── 📄 api.py                 # Flask API server
├── 📁 templates/
│   └── 📄 index.html         # Frontend interface
├── 📁 cipher/
│   ├── 📄 caesar.py          # Caesar cipher implementation
│   ├── 📄 vigenere.py        # Vigenère cipher implementation
│   ├── 📄 railfence.py       # Rail fence cipher implementation
│   ├── 📄 playfair.py        # Playfair cipher implementation
│   └── 📄 transposition.py   # Transposition cipher implementation
└── 📄 README.md
```

## 🚀 Hướng dẫn chạy ứng dụng

### 1. Cài đặt dependencies:

```bash
pip install flask
```

### 2. Chạy server:

```bash
python api.py
```

### 3. Truy cập ứng dụng:

Mở browser và truy cập: `http://127.0.0.1:5050`

## 📱 API Endpoints

### Caesar Cipher:

- `POST /api/caesar/encrypt` - Mã hóa
- `POST /api/caesar/decrypt` - Giải mã

### Vigenère Cipher:

- `POST /api/vigenere/encrypt` - Mã hóa
- `POST /api/vigenere/decrypt` - Giải mã

### Rail Fence Cipher:

- `POST /api/railfence/encrypt` - Mã hóa
- `POST /api/railfence/decrypt` - Giải mã

### Playfair Cipher:

- `POST /api/playfair/creatematrix` - Tạo ma trận
- `POST /api/playfair/encrypt` - Mã hóa
- `POST /api/playfair/decrypt` - Giải mã

### Transposition Cipher:

- `POST /api/transposition/encrypt` - Mã hóa
- `POST /api/transposition/decrypt` - Giải mã

## 📊 Request/Response Format

### Request Example:

```json
{
  "plain_text": "Hello World",
  "key": "secret"
}
```

### Response Example:

```json
{
  "encrypt_message": "Encrypted text here"
}
```

## 🎯 Mục tiêu học tập

- ✅ Hiểu và implement các thuật toán mật mã cổ điển
- ✅ Xây dựng RESTful API với Flask
- ✅ Thiết kế giao diện web hiện đại
- ✅ Tích hợp frontend và backend
- ✅ Áp dụng kiến thức bảo mật thông tin

## 📝 Ghi chú

Dự án được phát triển cho môn **Bảo Mật Thông Tin Nâng Cao** tại **Đại học Công nghệ TP.HCM (HUTECH)**. Tập trung vào việc hiểu sâu các thuật toán mật mã và ứng dụng thực tế.

## 📧 Liên hệ

**Email:** [student email]  
**GitHub:** [your github]

---

_© 2025 Tô Phạm Thành Đạt - HUTECH_
