class HashTable:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def insert(self ,key, value):
        self.key = key
        self.value = value
        return HashTable.insert(self.key,self.value)
    def find(self ,key):
        self.key = key
        return HashTable.find(self.value)
    phone_number={'aakash': "987654321"}
HashTable.find.self.value('aakash')
