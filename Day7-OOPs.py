'''
Object Oriented Programming

object - instance of a class
class - blueprint characterstics/data member/state | has functionality/member function/behaviour - actions contains verb

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


'''
relationship between classes / association

has a
has many

aggregation - weakly associated
 -> one class deleted the other class is not affected much

composition - strongly associated
 -> one class deleted the other class is affected a lot


-> one to one - Student : ID

class Student:
    def __init__(self, name, dept, idCard=None):
        self.name = name
        self.dept = dept
        self.idCard = idCard
    
    def __str__(self) -> str:
        return self.name+" - "+self.dept+" - "+str(self.idCard)

class IDCard:
    def __init__(self, rno, is_barcode):
        self.rno = rno
        self.is_barcode = is_barcode
    
    def __str__(self) -> str:
        return self.rno+" : "+str(self.is_barcode)

s = Student("Shivu", "AI&DS")
i = IDCard("21aib36", True)

s.idCard = i

print(s)

#another idea:
i = IDCard("21aib36", True)
s = Student("Shivu", "AI&DS", i)

print(s)

-> one to many - Book : Page

class Page:
    def __init__(self, pNO, content):
        self.pNo = pNO
        self.content = content
    
    def __str__(self):
        return str(self.pNo) + " - " + str(self.content)

class Book:
    def __init__(self, name, author, pages=[]):
        self.name = name
        self.author = author
        self.pages = pages
    
    def __str__(self) -> str:
        s = self.name + " : " + self.author + "\n"
        for i in self.pages:
            s += str(i)+"\n"
        return s

pages = []
pages.append(Page(1,"Hi "))
pages.append(Page(2,"Hello "))
pages.append(Page(3,"Welcome "))
pages.append(Page(4,"To "))
pages.append(Page(5,"Karigalan's"))
pages.append(Page(6,"MAgic"))
pages.append(Page(7,"Show "))

book = Book("Magic", "Shivu", pages)

print(book)

-> many to many - Teacher : Student

'''

class Teacher:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
    
    def __str__(self):
        return self.name + " : " + self.dept
    
class Student:
    def __init__(self, name, rno):
        self.name = name
        self.rno = rno
    
    def __str__(self) -> str:
        return self.name + " : " + str(self.rno)

class TeacherStudentMap:
    def __init__(self,teacher,student ):
        self.teacher = teacher
        self.student = student
    
    def __str__(self):
        return str(self.teacher)+" - "+str(self.student)

teachers = []
students = []
tsList = []

teachers.append(Teacher("T1", "AI"))
teachers.append(Teacher("T2", "DS"))
teachers.append(Teacher("T3", "Math"))
teachers.append(Teacher("T4", "PT"))

students.append(Student("S1", 121))
students.append(Student("S2", 122))
students.append(Student("S3", 123))
students.append(Student("S4", 124))
students.append(Student("S5", 125))

tsList.append(TeacherStudentMap(teachers[0],students[0]))
tsList.append(TeacherStudentMap(teachers[0],students[1]))
tsList.append(TeacherStudentMap(teachers[1],students[0]))
tsList.append(TeacherStudentMap(teachers[1],students[2]))
tsList.append(TeacherStudentMap(teachers[1],students[4]))
tsList.append(TeacherStudentMap(teachers[2],students[1]))
tsList.append(TeacherStudentMap(teachers[2],students[4]))
tsList.append(TeacherStudentMap(teachers[3],students[3]))

for i in tsList:
    print(i)


