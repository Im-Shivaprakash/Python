'''

Bitwise Operation reduces :
-> Time COmplexity
-> Space Complexity

'''

'''

Control Statements:

-> Conditional Statements :
    - simple if
    - if else
    - cascaded if else / if else ladder
    - nested if else
    
#Example code for the conditional statements
age = int(input("Enter the age: "))

if (age <= 120 and age >= 0):
    if age >= 25:
        print("Can vote and stand in election")
    elif age >= 18:
        print("Eligible to vote")
    else:
        print("Too young")
else:
    print("Invalid age")
    
print("Welcome")

'''

'''

-> Looping Statements:

    - for : used to iterate over the sequence types
    - while : general looping logics
    
    range - sequence generator
    range(start, end, step-size)


#example for range function usage:
for i in range(50, 60, 1):
    print(i, end = " ")
for i in range(50, 60):
    print(i, end = " ")
    

#example for nested looping:
r = 4
c = 5

for i in range(r): #rows
    for j in range(c): #columns
        print(i, j, sep=",", end = " ")
    print()


n = int(input("Enter the N : "))
for i in range(n): #next line taker
    for j in range(n): #value printer
        print(j, end = ' ')
    print()



n = int(input("Enter the N :"))
for i in range(1, n+1):
    for j in range(1, (n+1)-(n-i)): #my concept
        print(j, end = " ")
    print()


n = int(input("Enter the N :"))
for i in range(1, n+1):
    for j in range(1, i+1): #simplified concept
        print(j, end = " ")
    print()


while loop 

I - initialization
C - condition
U - updation

* These ICU are hidden in for loop

find the sum of the digits of a given integer

n = int(input())
sum_value = 0
while n!=0:
    d = n%10
    sum_value += d
    n //= 10
print(sum_value)


#Prime Number
n = int(input())
for i in range(2,n):
    if n%i == 0:
        print("Composite")
        break
    
else:
    print("Prime")

'''







'''
Assignment 1: (Conditional Statement)

    3 angles of triangle
    - equilateral 
    - isoceles
    - right isoceles
    - right scalene
    
    Classify the given degrees into what type of triangle

#CODE:

a, b, c = map(int, input("Enter the degrees : ").split())
sum_of_degree = a + b + c
if sum_of_degree <= 180 :

    if a == b and b == c :
        print("Equilateral Triangle")
        
    elif a == 90 or b == 90 or c == 90 :
        if a == b or b == c:
            print("Right Isoceles Triangle")
        else:
            print("Right Scalene Triangle")
    
    elif a == b or b == c :
        print("Isoceles Triangle")
    
    else:
        print("Scalene Triangle")

else:
    print("Enter valid angles")



Assignment 2: (Looping Statement)

    Print the pattern based on N (sample 5)
    * # # # *
    # * # * #
    # # * # #
    # * # * #
    * # # # *

i+j == n-1 (fill diagonal)


#my-code
pattern = [(1,1), (1,5), (2,2), (2,5), (3,3), (4,2), (4,4), (5,1), (5,5)]
for i in range(1, 6):
    for j in range(1, 6):
        if (i, j) in pattern:
            print('*',end = ' ')
        else:
            print('#', end = ' ')
    print()


#chatgpt-code
for i in range(5):
    for j in range(5):
        if i == j or i + j == 5:
            print('*', end=' ')
        else:
            print('#', end=' ')
    print()

Other patterns:

1)Jamaican Flag  

n = int(input())
for i in range(n):
    for j in range(n):
        if i == j or i + j == n-1:
            print('*', end = ' ')
        elif i>j and i+j > n-1:
            print("#", end = ' ')
        elif j>i and i+j < n-1:
            print("#", end = ' ')
        else:
            print('$', end = ' ')
    print()

2)

n = int(input())
for i in range(n):
    for j in range(n+1):
        if i == j or i > j :
            print("*", end = ' ')
        else:
            print("#", end = ' ')
    print()

3)

n = int(input())
for i in range(n):
    for j in range(n): #optimize - i+1 
        if i == j or i > j:
            print('#', end = ' ')
    print()

3)

n = int(input())
for i in range(n):
    for j in range(n): #optimize - n-i 
        if i == j or j > i:
            print('#', end = ' ')
    print()

4) South African Flag


'''

n = int(input())
for i in range(n):
    for j in range(n):
        if j < (n+1)//2:
            if i ==  j or i+j == n-1 :
                print("*", end = '  ')
            elif i > j and i+j < n-1 :
                print("-", end = '  ')
            elif j > i :
                print("#", end = '  ')
            else:
                print("$", end = '  ')
        else:
            if i < (n+1)//2 - 1 :
                print("#", end = '  ')
            elif i == (n+1)//2 - 1 :
                print("*", end = '  ')
            else:
                print("$", end = '  ')
        
    print()
