'''import MyModules as mm

print("Inside main")
a = int(input())
b = int(input())

c = mm.sum_of_two_numbers(a,b)
print("Sum = ", c)

print(mm.person['Address'])'''



from MyModules import sum_of_two_numbers, person
a = 5
b = 10
print(sum_of_two_numbers(a,b))
print(person['name'])