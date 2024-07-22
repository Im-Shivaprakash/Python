#creating a node:

class Node:
    
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

#creating a linked list with just head

class LinkedList:
    
    def __init__(self,head = None):
        self.head = head
    
    # adding an element at the end or appending
    def add_at_end(self, data):
        nn = Node(data)
        if self.head == None:
            self.head = nn
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = nn
    
    # adding an element at the head
    def add_at_head(self, data):
        nn = Node(data, self.head)
        self.head = nn
    
    # adding an element at the position
    def add_at_pos(self, data, pos):
        if self.head == None or pos == 0:
            nn = Node(data, self.head)
            self.head = nn
        else:
            temp = self.head
            counter = 0
            while counter < pos-2 :
                temp = temp.next
                counter+=1
            nn = Node(data, temp.next)
            temp.next = nn
    
    # adding an element after the position
    def add_after_pos(self, data, pos):
        self.add_at_pos(data,pos+1)
    
    #adding an element in ascending order
    def add_in_asc(self,data):
        nn = Node(data)
        temp = self.head
        if self.head == None:
            self.head = nn
        else:
            if data < temp.data:
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
    
    #delete an element at the end
    def delete_at_end(self):
        if self.head == None:
            print("Linkedlist is empty")
        else:
            temp = self.head
            if temp.next == None:
                self.head == None
            else:
                prev = None
                while temp.next!=None:
                    prev = temp
                    temp = temp.next
                prev.next = None
    
    #delete at the head
    def delete_at_head(self):
        self.head = self.head.next
    
    #delete at the pos
    def delete_at_pos(self, pos):
        temp = self.head
        if self.head == None:
            print("Linkedlist is empty")
        else:
            if pos == 0:
                self.delete_at_head()
            else:
                prev = None
                counter = 0
                while counter < pos-1:
                    prev = temp
                    temp = temp.next
                    counter+=1
                prev.next = temp.next
    
    #delete after pos
    def delete_after_pos(self, pos):
        self.delete_at_pos(pos+1)
    
    #search the element
    def search_ll(self, data):
        temp = self.head
        counter = 1
        if temp == None:
            print("Empty LinkedList")
            return
        else:
            while temp != None:
                if temp.data == data:
                    print(counter)
                    break
                else:
                    temp = temp.next
                    counter += 1
            if temp == None:
                print("Element ",data," not found")
                
    # update via element search
    def update_ele_ll(self, data, value):
        temp = self.head
        if temp == None:
            print("Empty LinkedList")
            return
        else:
            while temp != None:
                if temp.data == data:
                    temp.data = value
                    break
                else:
                    temp = temp.next
            if temp == None:
                print("Out of bounds")
                
    #update via pos search:
    def update_pos_ll(self, data, pos):
        temp = self.head
        counter = 1
        if temp == None:
            print("Empty Linkedlist")
            return
        while temp != None and counter < pos:
            temp = temp.next
            counter += 1
        if temp == None:
            print("Out of bounds")
        else:
            temp.data = data
    
    #printing the linked_list 
    def __str__(self):
        s = ''
        temp = self.head
        while temp != None:
            s += str(temp.data)+'  ->  '
            temp = temp.next
        return s

ll = LinkedList()

# ll.add_at_end(2)
# print(ll)
# ll.add_at_end(3)
# print(ll)
# ll.add_at_end(4)
# print(ll)
# ll.add_at_end(6)
# print(ll)
# ll.add_at_head(1)
# print(ll)
# ll.add_at_pos(5,5)
# print(ll)
# ll.add_after_pos(7,6)
# print(ll)

# ll.add_in_asc(1)
# print(ll)
# ll.add_in_asc(2)
# print(ll)
# ll.add_in_asc(5)
# print(ll)
# ll.add_in_asc(3)
# print(ll)
# ll.add_in_asc(4)
# print(ll)

ll.add_at_end(1)
print(ll)
ll.add_at_end(2)
print(ll)
ll.add_at_end(3)
print(ll)
ll.add_at_end(4)
print(ll)
ll.add_at_end(5)
print(ll)
ll.add_at_end(6)
print(ll)
ll.add_at_end(7)
print(ll)

# ll.delete_at_end()
# print(ll)
# ll.delete_at_head()
# print(ll)

# ll.delete_at_pos(5)
# print(ll)
# ll.delete_after_pos(5)
# print(ll)
# ll.delete_at_pos(0)
# print(ll)

# ll.search_ll(5)
# ll.search_ll(10)

# ll.update_ele_ll(5, 50)
# print(ll)
# ll.update_ele_ll(10, 50)
# print(ll)

ll.update_pos_ll(50, 50)
print(ll)
