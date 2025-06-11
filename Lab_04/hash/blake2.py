import hashlib

def blake2_hash(message):

    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message)
    return blake2_hash.digest()

def main():
    text = input("Nhập chuỗi cần băm BLAKE2: ").encode('utf-8')
    hash_value = blake2_hash(text)
    print("Chuỗi đã nhập :", text.decode('utf-8'))
    print("Mã băm BLAKE2 của chuỗi:", hash_value.hex())

if __name__ == "__main__":
    main()
