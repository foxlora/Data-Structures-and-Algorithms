class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class LinkedList(object):
    def __init__(self):
        self.head = None

    def __repr__(self):
        tmp = self.head
        if tmp:
            return "{} -> {}".format(tmp.val, tmp.next)



    #在开头插入
    def push(self,data):
        NewNode = ListNode(data)
        NewNode.next = self.head
        self.head = NewNode

    #在末尾插入
    def insert(self,data):
        self.head = self.__insert(self.head,data)

    def __insert(self,head,data):
        if not head:
            head = ListNode(data)
        else:
            head.next = self.__insert(head.next,data)

        return head

    #翻转链表
    def __reversed__(self):
        prev = None
        current = self.head
        while current:
            dummy = current.next

            current.next = prev
            prev = current

            current = dummy


        self.head = prev

    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print("Found Loop")
                return




if __name__ == "__main__":
    linklist = LinkedList()
    linklist.insert(5)
    linklist.insert(3)
    linklist.insert(4)
    linklist.insert(7)
    linklist.insert(8)
    #linklist.head.next.next.next.next.next = linklist.head



    print(linklist)


