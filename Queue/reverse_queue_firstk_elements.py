from queue import Queue



def Reverse_Queue_FirstK_Elements(k,Queue):
    if Queue.empty() or k > Queue.qsize():
        return
    if k <= 0:
        return

    stack = []

    for i in range(k):
        stack.append(Queue.get())

    while len(stack):
        Queue.put(stack.pop())

    for i in range(Queue.qsize() - k):
        Queue.put(Queue.get())

def Print_Queue(Queue):
    while not Queue.empty():
        print(Queue.get(),end=" ")


if __name__ == "__main__":
    Queue = Queue()
    Queue.put(10)
    Queue.put(20)
    Queue.put(30)
    Queue.put(40)
    Queue.put(50)
    Queue.put(60)

    k = 4

    Reverse_Queue_FirstK_Elements(k,Queue)
    Print_Queue(Queue)