import hashlib
from block import block


class chain:

    def __init__(self,difficulty):
        self.difficulty=difficulty
        self.blocks=[]
        self.pool=[]
        self.create_originblock()
    

    def proof_of_work(self,block):
        hash=hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        return block.hash==hash.hexdigest() and int(hash.hexdigest(),16) < 2**(256-self.difficulty) and block.prev_hash==self.blocks[-1].hash
    
    def add_to_chain(self,block):
        if self.proof_of_work(block):
            self.blocks.append(block)

    def add_to_pool(self,data):
        self.pool.append(data)
    
    def create_originblock(self):
        h=hashlib.sha256()
        h.update(''.encode('utf-8'))
        origin=block("origin",h.hexdigest())
        origin.mine(self.difficulty)
        self.blocks.append(origin)
        
    def mine(self):
        if self.pool:
            data=self.pool.pop()
            b=block(data,self.blocks[-1].hash)
            b.mine(self.difficulty)
            self.add_to_chain(b)
            print("hash : \t\t",b.hash)
            print("previous hash : \t\t",b.prev_hash)
            print("nonce :\t\t",b.nonce)
            print("data :\t\t",b.data)
        


        


