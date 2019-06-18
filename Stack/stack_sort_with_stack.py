'''
用一个临时栈为一个栈排序
'''

class Stack(object):
    def __init__(self,):
        self.array = []



    def isEmpty(self):
        if self.array:
            return False
        else:
            return True

    def pop(self):
        if not self.isEmpty():
            return self.array.pop()
        else:
            return "$"

    def push(self,op):
        self.array.append(op)

    def top(self):
        if not self.isEmpty():
            return self.array[-1]



#本质是插入排序
def sortStack(stk):
    tmpStack = Stack()
    while not stk.isEmpty():
        tmp = stk.pop()

        # while temporary stack is not
        # empty and top of stack is
        # greater than temp
        while not tmpStack.isEmpty() and int(tmpStack.top()) < int(tmp):
            stk.push(tmpStack.pop())

        tmpStack.push(tmp)

    return tmpStack


stk = Stack()
stk.push(5)
stk.push(4)
stk.push(3)
stk.push(7)
stk.push(8)

res = sortStack(stk)

while not res.isEmpty():
    print(res.pop())


