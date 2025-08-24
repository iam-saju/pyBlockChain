import hashlib


class block:

    def __init__(self,data,prev_block):
        self.data=data
        self.hash=None
        self.nonce=0
        self.prev_hash=prev_block
    def __str__(self):#runs when print(block) is called
        return f'{self.data}{self.nonce}{self.prev_hash}'
    
    def mine(self, difficulty):
        while True:
            hash_value = hashlib.sha256(str(self).encode('utf-8')).hexdigest()
            if int(hash_value, 16) < 2**(256 - difficulty):
                self.hash = hash_value  # store final string, not hash object
                break
            self.nonce += 1

