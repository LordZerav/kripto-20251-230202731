import hashlib
import time


class SimpleBlock:
    def __init__(self, number, payload, prev_hash):
        self.number = number
        self.payload = payload
        self.prev_hash = prev_hash
        self.created_at = time.time()
        self.nonce = 0
        self.current_hash = self.generate_hash()

    def generate_hash(self):
        raw_data = (
            str(self.number) +
            str(self.payload) +
            str(self.prev_hash) +
            str(self.created_at) +
            str(self.nonce)
        )
        return hashlib.sha256(raw_data.encode()).hexdigest()

    def proof_of_work(self, level):
        target = "0" * level
        while not self.current_hash.startswith(target):
            self.nonce += 1
            self.current_hash = self.generate_hash()
        print(f"Block #{self.number} berhasil ditambang")
        print(f"Hash : {self.current_hash}\n")


class MiniBlockchain:
    def __init__(self):
        self.blocks = []
        self.level = 4
        self.init_chain()

    def init_chain(self):
        genesis = SimpleBlock(0, "Genesis Block", "0")
        genesis.proof_of_work(self.level)
        self.blocks.append(genesis)

    def latest_hash(self):
        return self.blocks[-1].current_hash

    def insert_block(self, info):
        index = len(self.blocks)
        new_block = SimpleBlock(index, info, self.latest_hash())
        new_block.proof_of_work(self.level)
        self.blocks.append(new_block)


# uji simulasinya
chain = MiniBlockchain()

chain.insert_block("A kirim 10 coin ke B")
chain.insert_block("B kirim 5 coin ke C")