'''

- > Sequence types:

CRUD Operations:
Create
Read
Update
Delete

1) LIST:
* []
* mutable - can modify
* list() - constructor

t = (1,2,3,4)
print(t)
l = list(t)
print(l)
print(type(l))

* heterogeneous


CREATE & READ

list1 = [1, 2, 3, 4, [11, 12, 13], "hi", "hello", [12.3, 13.4, [90]]]
print(list1[5])
print(list1[6][2])
print(list1[6][-1])

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l[2:6])
print(l[1::2])
print(l[::-1])
print(l[-1:-8:-1])

UPDATE

- append function:

n = int(input())
l = []
for i in range(n):
    d = int(input())
    l.append(d)
    print(l)
print(l)

- insert function :

l = [1,2,3,4,5]
l.insert(2, 2.5)
print(l)

- extend function :

l = [1,2,3,4,5]
l.extend([6,7,8,9,10])
print(l)

l = [1,2,3,4,5]
l.append([6,7,8,9,10])
print(l)

- Membership operator

l = [1,2,3,4]
for i in l:   # membership operator - (in)
    print(i)

print(23 not in l)

- Memory Allocation :

l1 = [1,2,3]
l2 = [4,5,6]
l = l1+l2
print(l)
print(id(l1))
print(id(l2))
print(id(l))

l1 = [1,2,3]
l2 = l1
print(id(l1))
print(id(l2))
l1[1] = 'two'
print(l1)
print(l2)

l1 = [1,2,3]
l2 = l1.copy()
print(id(l1))
print(id(l2))
l1[1] = 'two'
print(l1)
print(l2)

- Repetition Operator :

l = []
for i in range(100):
    l.append(0)
print(l)

l = [0] * 100 (* -> Repetitive Operator)
print(l)

DELETE

- Remove Function:

l = [1,2,3,4]
print(l)
l.remove(2)
print(l)

l = [1,2,3,4,2]
print(l)
l.remove(l[4])
print(l)

l = [1,2,3,4,2]
print(l)
del(l[4])
print(l)

l.clear()
print(l)

del(l)
print(l)

l = [1,2,3,4,2]
print(l)
l.pop() #by default last value
print(l)


2) TUPLE :

* ()
* immutable
* tuple() - type convertor

l = [1,2,3,4,2]
t = tuple(l)
print(t)
print(type(t))

* heterogeneous

t = (1, 2, 3, 4, (11, 12, 13), "hi", "hello", (12.3, 13.4, (90,91)))
print(t[7])

DELETION :

t = (1,2,[12,34,56],(321,543))
print(t)
t[2][1] = 43  # memory allocataion is the key 
print(t)

T = (1,2,3)
del(t)
print(T)

* Single Element Tuple

l = [1]
t = (1)
tu = (1,)
print(t)
print(type(t))
print(tu)
print(type(tu))

* Tuple Updation - 

1. Tuple Concatenation:

t = ()
n = 5
for i in range(n):
    d = int(input())
    temp = (d,)
    t = t+temp
    print(t)

2. List to Tuple Conversion:

l = [0] * 100
print(l)
t = tuple(l)
print(t)



'''



