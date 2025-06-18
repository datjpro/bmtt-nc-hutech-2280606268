from blockchain import Blockchain
import json
import time

def print_separator():
    print("=" * 60)

def display_block(block, block_num):
    print(f"📦 BLOCK #{block_num}")
    print(f"🕐 Timestamp: {time.ctime(block.timestamp)}")
    print(f"🔗 Previous Hash: {block.previous_hash[:20]}...")
    print(f"🎯 Hash: {block.hash[:20]}...")
    print(f"🏭 Proof of Work: {block.proof}")
    print(f"💼 Transactions ({len(block.transactions)}):")
    
    if block.transactions:
        for i, tx in enumerate(block.transactions, 1):
            print(f"   {i}. {tx['sender']} → {tx['receiver']}: {tx['amount']} coins")
    else:
        print("   (Genesis Block - No transactions)")
    print()

def main():
    print_separator()
    print("🚀 BLOCKCHAIN DEMO - HUTECH CYBERSECURITY LAB")
    print_separator()
    
    # Khởi tạo blockchain
    print("🔧 Initializing blockchain...")
    blockchain = Blockchain()
    print("✅ Blockchain initialized with Genesis block")
    print()
    
    # Thêm các giao dịch
    print("💰 Adding transactions...")
    blockchain.add_transaction("Alice", "Bob", 50)
    blockchain.add_transaction("Bob", "Charlie", 25)
    blockchain.add_transaction("Charlie", "David", 10)
    print("✅ Added 3 transactions to pending pool")
    print()
    
    # Mining block đầu tiên
    print("⛏️ Mining first block...")
    start_time = time.time()
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block.proof
    new_proof = blockchain.proof_of_work(previous_proof)
    mining_time = time.time() - start_time
    
    # Thêm reward cho miner
    blockchain.add_transaction("System", "Miner_Alice", 12.5)
    new_block = blockchain.create_block(new_proof, previous_block.hash)
    
    print(f"✅ Block mined successfully in {mining_time:.2f} seconds")
    print(f"🎯 Proof of Work found: {new_proof}")
    print()
    
    # Thêm thêm giao dịch cho block thứ 2
    print("💰 Adding more transactions...")
    blockchain.add_transaction("David", "Eva", 15)
    blockchain.add_transaction("Eva", "Frank", 8)
    blockchain.add_transaction("Frank", "Alice", 3)
    print("✅ Added 3 more transactions")
    print()
    
    # Mining block thứ 2
    print("⛏️ Mining second block...")
    start_time = time.time()
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block.proof
    new_proof = blockchain.proof_of_work(previous_proof)
    mining_time = time.time() - start_time
    
    blockchain.add_transaction("System", "Miner_Bob", 12.5)
    new_block = blockchain.create_block(new_proof, previous_block.hash)
    
    print(f"✅ Block mined successfully in {mining_time:.2f} seconds")
    print(f"🎯 Proof of Work found: {new_proof}")
    print()
    
    # Hiển thị toàn bộ blockchain
    print_separator()
    print("📋 COMPLETE BLOCKCHAIN")
    print_separator()
    
    for i, block in enumerate(blockchain.chain):
        display_block(block, i + 1)
    
    # Kiểm tra tính hợp lệ
    print_separator()
    print("🔍 BLOCKCHAIN VALIDATION")
    print_separator()
    
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        print("✅ Blockchain is VALID")
        print("🔒 All blocks are properly linked")
        print("🎯 All proofs of work are correct")
    else:
        print("❌ Blockchain is INVALID")
        print("🚨 Chain has been tampered with!")
    
    print()
    print_separator()
    print("📊 BLOCKCHAIN STATISTICS")
    print_separator()
    print(f"📦 Total Blocks: {len(blockchain.chain)}")
    
    total_transactions = sum(len(block.transactions) for block in blockchain.chain)
    print(f"💼 Total Transactions: {total_transactions}")
    
    # Tính tổng coins đã transfer
    total_amount = 0
    for block in blockchain.chain:
        for tx in block.transactions:
            if tx['sender'] != 'System':  # Không tính reward
                total_amount += tx['amount']
    
    print(f"💰 Total Coins Transferred: {total_amount}")
    print(f"🏆 Mining Rewards Issued: {total_transactions - total_amount}")
    
    print()
    print_separator()
    print("🎉 DEMO COMPLETED SUCCESSFULLY!")
    print_separator()

if __name__ == "__main__":
    main()
