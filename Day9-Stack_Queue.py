'''

Stack - LIFO (CD Tray)

push - inserting a new element
pop - removing an element at the top

top default element = -1 on a empty stack
can only remove the top element



'''

class Stack:
    def __init__(self,ms):
        self.ms = ms
        self.top = -1
        self.s = []

    def push(self,ele):
        if self.top == self.ms-1:
            print("Stack Overflow")
        else:
            self.s.append(ele)
            self.top += 1

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            self.top -= 1
            d = self.s.pop()
            return d

    def __str__(self) -> str:
        return str(self.s)

stack = Stack(3)
print(stack.pop())
stack.push(5)
print(stack)
stack.push(10)
print(stack)
stack.push(15)
print(stack)
stack.push(20)
print(stack)

stack.pop()
print(stack)
stack.pop()
print(stack)

'''

Queue - FIFO

front = -1
rear = -1

enqueue - add one ele at a time
dequeue - remove one ele at a time

* only time when the front and rear changes is when there is only one element added into the queue from empty



'''

class Queue:
    def __init__(self, ms):
        self.ms = ms
        self.front = -1
        self.rear = -1
        self.q = []
        
    def enq(self, ele):
        if self.rear == self.ms-1:
            print("Queue is full")
        else:
            self.q.append(ele)
            if self.front == -1:
                self.front = 0
            self.rear += 1
            
    def deq(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        elif self.rear == 0:
            self.front = self.rear = -1
        else:
            self.rear -= 1
        return  self.q.pop(0)
    
    def __str__(self):
        return str(self.q)

queue = Queue(3)
print(" The Dequeue element is ",queue.deq())
print(queue)

queue.enq(5)
print(queue)
queue.enq(10)
print(queue)
queue.enq(15)
print(queue)
queue.enq(20)
print(queue)
queue.deq()
print(queue)

'''

Linked list implementation:

Stack:
top = head
push = add at beginning
pop = delete at beginning

Queue:
front = head
eQ = add at end
deQ = remove at beginning

'''