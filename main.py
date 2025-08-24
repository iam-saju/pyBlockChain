from chain import chain

eth=chain(20)
i=0 

while i<=5:
    eth.add_to_pool(str(i))
    eth.mine()
    print("\n","="*10,"\n")
    i+=1


 