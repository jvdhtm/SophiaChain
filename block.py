from hashlib import sha256


def UpdateHash(*args):

    hashingText = ""
    h = sha256()

    for arg in args:
        hashingText += str(arg)
    h.update(hashingText.encode('utf-8'))
    return h.hexdigest

class Block():
    data = None
    hash = None
    nonce = 0
    prevHash = "0" * 256
    def __init__(self, data, number = 0) :
        self.data = data
        self.number =  number
    def hash(self) :
         return UpdateHash(self.prevHash, self.number, self.data, self.nonce)

class BlockChain():
    pass

def main():
    return
    
if __name__ == '__main__':
    main()
