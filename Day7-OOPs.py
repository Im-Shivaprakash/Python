'''
Object Oriented Programming

object - instance of a class
class - blueprint characterstics/data member/state | has functionality/member function/behaviour

'''


'''
class Person:
    def __init__(self, age, gender, height, weight):  #constructor
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        name = "JK"
    
    def display(s): #must use self as the first argument , can be name changed
        print("Person Details:")
        print("Age=", s.age)
        print("Gender=", s.gender)
        print("Height=", s.height)
        print("Weight=", s.weight)
    
    def __str__(self):
        return str(self.age) + "," + self.gender + ',' + str(self.height) + ',' + str(self.weight)
    

p1 = Person(25,'M',165,60)  #throws error if not all given , can make use of default arguments
p2 = Person(23, 'F', 160, 49)

p1.display()
p2.display()

print(p1)

'''

'''
Access Specifiers:

public - no underscore - can be accessed by anywhere
protected - one underscore - should be accessed by the inherited classes
private - two underscores - should not be accessed anywhere except in the same class

'''

'''

class Person:
    def __init__(self, age, height, gender):
        self.age = age
        self._height = height
        self.__gender = gender

p = Person(27, 178, "M")

print(p.age)
print(p._height)

#accessing private variable using name mangling
print(p._Person__gender)

'''

'''
Getter Setter:

get() - get from the class
set() - update the class

'''
'''

class Person():
    def __init__(self, age):
        self.age = age
    
    def get_age(self):
        return self.age
    
    def set_age(self,age):
        self.age = age
        
    def __str__(self) -> str:
        return "age = "+str(self.age)
        
p = Person(45)
print(p.get_age())
p.set_age(27)
print(p)

'''

'''using @property'''

# #Type 1:
# class Person():
#     def __init__(self, age):
#         self._age = age
    
#     def get_age(self):
#         print("Inside Age Getter\n")
#         return self.age
    
#     def set_age(self,age):
#         print("Inside Age Setter\n")
#         self.age = age
    
#     def del_age(self):
#         del self.age
    
#     def __str__(self) -> str:
#         return "age = "+str(self.age)
    
#     age_fix = property(get_age, set_age, del_age)
    
# p = Person(25)
# p.age_fix = 27
# print(p.age_fix)
# print(p)


# #Type 2:
# class Person():
#     def __init__(self, age):
#         self._age = age
    
#     def get_age(self):
#         print("Inside Age Getter\n")
#         return self._age
    
#     def set_age(self,age):
#         print("Inside Age Setter\n")
#         self._age = age
    
#     def del_age(self):
#         del self._age
    
#     def __str__(self):
#         return "age = "+str(self._age)
    
#     age_fix = property(get_age, set_age, del_age)
    
# p = Person(25)
# print(p)
# p.age = 27
# print(p.age)
# print(p)

# #Type 3:
# class Person():
#     def __init__(self, age):
#         self._age = age
    
#     @property
#     def age(self):
#         print("inside getter")
#         return self._age
    
#     @age.setter
#     def age(self, age):
#         print("Inside Setter")
#         self._age = age

#     def __str__(self):
#         return "age = "+str(self._age)
    
# p = Person(25)
# print(p)
# p.age = 27
# print(p.age)
# print(p)

