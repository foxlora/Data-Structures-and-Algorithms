class Trie(object):
    def __init__(self):
        self.root = {}
        self.end = -1

    def insert(self,word):

        curNode = self.root
        for c in word:
            if not c in curNode:
                curNode[c] = {}
            curNode = curNode[c]
        curNode[self.end] = True


    def search(self,word):
        curNode = self.root
        for c in word:
            if not c in curNode:
                return False
            curNode = curNode[c]

        if not self.end in curNode:
            return False
        return True

    def startWith(self,prefix):
        curNode = self.root
        for c in prefix:
            if not c in curNode:
                return False
            curNode = curNode[c]
        return True


if __name__ == "__main__":
    obj = Trie()
    obj.insert('xlf')
    obj.insert('xlf love jiafan')
    obj.insert("xlf love freedom")
    print(obj.search("xlf"))

