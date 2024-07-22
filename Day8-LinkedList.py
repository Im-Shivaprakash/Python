'''
Data Structures

CRUD 

Create 
Read / Search / Retrieve
Update
Delete

list
stack
queue
tree
graph
hash table

Storage structures
list
Linked list

'''

'''
LINKED LIST

insert :
    append - y
    add at beginning - y
    add at position - y
    adding after position - n
    add in asc order - y

delete:
    deletion at end - y
    delete at beginning - y
    delete at position - y
    delete after position - n

search - n
update(in normal ll) - n
reverse - y
rotate:
    fully - y
    particular set of range - y

'''



'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self,data):
        # create a new node, fill the node, add it to the existing ld_list
        temp = self.head
        nn = Node(data)
        if self.head == None:
            self.head = nn
        else:
            while temp.next!= None:
                temp = temp.next
            temp.next = nn
    
    def add_at_beg(self,data): # using temp variable
        temp = self.head 
        nn = Node(data)
        if self.head == None:
            self.head = nn
        else:
            self.head = nn
            self.head.next = temp
    
    def add_at_beg_alt(self,data):
        nn = Node(data,self.head)
        self.head = nn
    
    def add_at_pos(self, data, pos): #iterate pos-2 times
        nn = Node(data)
        if pos == 1:
            nn.next = self.head
            self.head = nn
        else:
            temp = self.head
            counter = 0
            while counter < pos-2:
                if temp == None:
                    break
                temp = temp.next
                counter+=1
            if temp == None:
                print("Invalid Position")
            else:
                nn.next = temp.next
                temp.next = nn

    def __str__(self):
        s = ""
        temp = self.head
        while temp!= None:
            s += str(temp.data)+" "
            temp = temp.next
        return s

ld_list = LinkedList()
ld_list.append(5)
ld_list.append(15)
ld_list.append(20)
ld_list.append(25)
ld_list.append(35)
print(ld_list)

ld_list.add_at_pos(30,5)
print(ld_list)

ld_list.add_at_pos(100,50)
print(ld_list)

'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_in_asc(self,data):
        nn = Node(data)
        temp = self.head
        if self.head == None:
            self.head = nn
        else:
            if data < self.head.data:
                nn.next = self.head
                self.head = nn
            else:
                prev = None
                while temp.data < data:
                    prev = temp
                    temp = temp.next
                    if temp == None:
                        break
                nn.next = temp
                prev.next = nn
                
    
    def __str__(self):
        s = ""
        temp = self.head
        while temp!= None:
            s += str(temp.data)+" "
            temp = temp.next
        return s

ld_list = LinkedList()
ld_list.add_in_asc(1)
print(ld_list)
ld_list.add_in_asc(2)
print(ld_list)
ld_list.add_in_asc(5)
print(ld_list)
ld_list.add_in_asc(3)
print(ld_list)
ld_list.add_in_asc(4)
print(ld_list)