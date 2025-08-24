import hashlib

class node:

    def __init__(self,data):
        self.data=data
        self.next=None

n1=node(1)
n2=node(2)
n3=node(3)
n1.next=n2
n2.next=n3
"""
node traversal
n=n1
while(n):
    print(n.data)
    n=n.next
"""
h=hashlib.sha256()
h.update(b"hello world")
print(h.hexdigest())

i=0 
h.update(str(i).encode('utf-8'))
while(int(h.hexdigest(),16) > 2**(256-10)):
    i+=1
    h.update(str(i).encode('utf-8'))
print(i)#504

print(int(h.hexdigest(),16)," -> ",h.hexdigest())
h.update(b'504')
print(h.hexdigest())
