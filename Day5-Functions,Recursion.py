'''
Functions

- piece of code with a specific function to perform
- reusability
- name must be the actions it performs
- modular

Types:
1) Inbuilt
2) User-defined

Syntax:
def functionName(args): #first letter should be small - camel case

def function_name(args): - snake case

Works:
Stack Model - LIFO

Types:
1) Required Args
2) default args
3) Keyword Args
4) variable - length args

'''

'''
REQUIRED ARGS:

def sum_of_two_numbers(a,b):
    print("inside sum function")
    c = a+b
    return c    #default return is None

print("inside main function")
a = 5
b = 10
c = sum_of_two_numbers(a,b)
print("Sum =", c)     #function call searches above the line

'''

'''
KEYWORD ARGS

def sum(b,a): #changed position 
    print('a=', a)
    print('b=',b)
    c = a+b
    return c

x = 5
y = 10
d = sum(a=x, b=y) # searches for a in the args and assigns rather than the position
print(d)

'''

'''
DEFAULT VALUE

def sum(a,b = 10):
    c = a+b
    return c

x = 5
c = sum(x)
print("Sum", c)

y = 20
d = sum(x,y)
print("Sum", d)

'''

'''
VARIABLE LENGTH ARGS

def sum(*a): #type=tuple
    print(a)
    print(type(a))


d = sum(1,2,3,4,5,6,7,8,9,10)
print('d=', d)

'''

'''
def fun(l1):
    l1 = [3,4,5,6]
    print(l1)

L = [1,2,3,4]
print(L)
fun(L)
print(L)

'''

'''

Recursion :
- function calling (copy) itself
- iterative 
- simple code 
- bad for memory (new memory created)
- bad for time (allocation and deallocation)

Base Code:
def fun(args):
    if (base/exit condition):
        stmts
        return
    
    return recursive call/calls #if return not put here , output will be none

'''
'''
#factorial:
def facTorial(n):
    if n==0 or n==1 :
        return 1
    return n * facTorial(n-1)

num = 5
f = facTorial(num)
print(f)

'''

'''
#fibonacci series:
def fib(num):
    if num == 0:
        return 0
    
    if num == 1:
        return 1
    return fib(num-1) + fib(num-2)


num = 5
fib_ser = fib(num)
print(fib_ser)

'''

'''
#combination:
def comb(n, r):
    if n == r or r == 0:
        return 1
    if r == 1:
        return n
    return comb(n-1,r)+comb(n-1, r-1)

n = int(input())
r = int(input())
print(comb(n,r))

'''
