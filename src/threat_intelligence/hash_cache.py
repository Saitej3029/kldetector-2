import os
import hashlib

class HashCache:
    def __init__(self, cache_file='hash_cache.txt'):
        self.cache_file = cache_file
        self.hashes = self.load_hashes()

    def load_hashes(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as f:
                return set(line.strip() for line in f if line.strip())
        return set()

    def add_hash(self, item_hash):
        self.hashes.add(item_hash)
        self.save_hashes()

    def save_hashes(self):
        with open(self.cache_file, 'w') as f:
            for item_hash in self.hashes:
                f.write(f"{item_hash}\n")

    def contains(self, item_hash):
        return item_hash in self.hashes

    @staticmethod
    def calculate_hash(data):
        return hashlib.sha256(data.encode()).hexdigest()