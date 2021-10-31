from __future__ import print_function
import datetime
import hashlib
import json
import random


def actualTime():
    moment = datetime.datetime.now()
    stamp = str(str(moment.year) + str(moment.month) + str(moment.day) + str(moment.hour)
                + str(moment.minute) + str(moment.second) + str(moment.microsecond))
    return stamp

class Block(object):

    def hashMake(self):
        retezec = str(str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.nonce))
        encoder = retezec.encode()
        return hashlib.sha256(encoder).hexdigest()

    def __init__(self, data, previousHash):
        self.timeStamp = actualTime()
        self.data = str(data)
        self.previousHash = previousHash
        self.hash = ""
        self.nonce = 0


    def mineBlock (self, difficulty):
        zeros = difficulty * "0"
        while True:
            self.nonce = random.randint(1, 2**32)
            self.hash = self.hashMake()
            check = str(self.hash[:difficulty])
            if check == zeros:
                return



def blockchainDecoder (blockchain):
    if isinstance(blockchain,Block):
        printList = {"data": blockchain.data, "timestamp": blockchain.timeStamp, "previousHash": blockchain.previousHash,
        "hash": blockchain.hash}
        return printList

def jsoner():
    with open("data_file.json", "w") as writefile:
        json.dump(blockchain, writefile, sort_keys=True, separators=(',', ':'), indent= 4, default= blockchainDecoder)

    handle = open("data_file.json", "r")
    for line in handle:
        print(line, end=' ')

def isChainValid(first, second, third):
    if isinstance(first, Block) and isinstance(second, Block) and isinstance(third, Block):
        if (first.hash != second.previousHash or second.hash != third.previousHash):
            return "False"
        chekker = [first.hash, second.hash, third.hash]
        retezec1 = str(str(first.timeStamp) + str(first.data) + str(first.previousHash) + str(first.nonce))
        encoder1 = retezec1.encode()
        result1 = hashlib.sha256(encoder1).hexdigest()
        if(result1 != first.hash):
            return "False"
        retezec2 = str(str(second.timeStamp) + str(second.data) + str(second.previousHash) + str(second.nonce))
        encoder2 = retezec2.encode()
        result2 = hashlib.sha256(encoder2).hexdigest()
        if(result2 != second.hash):
            return "False"
        retezec3 = str(str(third.timeStamp) + str(third.data) + str(third.previousHash) + str(third.nonce))
        encoder3 = retezec3.encode()
        result3 = hashlib.sha256(encoder3).hexdigest()
        if(result3 != third.hash):
            return "False"
        return "True"
    return "False"


difficulty = 6
blockchain = []

blockchain.append(Block("Ahoj, ja jsem prvni blok", "0"))
print("Tezim blok 1... ")
blockchain[0].mineBlock(difficulty)
print("Blok vytezen! " + blockchain[0].hash)

blockchain.append(Block("Ja jsem druhy", blockchain[0].hash))
print("Tezim blok 2... ")
blockchain[1].mineBlock(difficulty)
print("Blok vytezen! " + blockchain[1].hash)
blockchain.append(Block("A ja treti", blockchain[1].hash))
print("Tezim blok 3... ")
blockchain[2].mineBlock(difficulty)
print("Blok vytezen! " + blockchain[2].hash)

print("Blockchain je platny: " + isChainValid(blockchain[0], blockchain[1], blockchain[2]))

print("Blockchain:")
jsoner()