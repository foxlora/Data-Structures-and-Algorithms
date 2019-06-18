'''
后缀表达式的求值
'''
class Stack(object):
    def __init__(self,):
        self.array = []
        self.top = -1


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


def Evaluation_of_postfix_expression(exp):
    stack_exp = Stack(len(exp))
    for i in exp:
        if i.isdigit():
            stack_exp.push(i)
        else:
            val1 = stack_exp.pop()
            val2 = stack_exp.pop()
            res = str(eval(val2+i+val1))
            stack_exp.push(res)

    return stack_exp.pop()

if __name__ == "__main__":
    exp = "231*+9-"
    res = Evaluation_of_postfix_expression(exp)
    print(res)