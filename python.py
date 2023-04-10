print('Hello','Maddy',sep = '_',end='your')
print(" Welcome "*3)  #string replication

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print("// used to avoid the . value and gives the output in int format : ",a//b)
print("% moudulo function used to show the remainder : ", a%b)

x = 20
x+=2 #augumentes assignment operator
print(x) 

r = 10
rr = r**5
r%=rr
print(r)

n = 25
print(n%2==0 or n%3==0)

conditional statements

if 10>5 and 10>6:
    print("true")


try:
    def fact(n):
        if n == 1:
            return n
        else:
            return n*fact(n-1)

except Valueerror as error:
    print(error)

finally :
    print(fact)
            

loops

for i in range(0,10,2): #(initial,end,step)
    print("Even",i)
    print("Odd",i+1)


for i in range(0,10,2): #(initial,end,step)
    print(i,end=' ')

i = 0
while i < 10:
    print(i)
    i = i+1

nums = [10,12,13,14,15]  # it shows all the values
for num in nums:
    if num % 5 == 0:
        print(num)  #to get the first value of list
        break

for num in nums:
    if num % 5 == 0:
        print(num)



for i  in enumerate(string):
    print(i)


datas = ['Maddy','Mathu','Onnum illa']
a = datas[0]

for data in enumerate(datas):
    print(data)

for j in enumerate(a):
    print(j)


for count,data in enumerate(datas,101):
    print(count,data)

for count,data in enumerate(datas,1001):
    print(count)
    print(data)


List comprehensions instead of raw for loops


numbers = [numb for numb in range(10)]
print(numbers)

list_data = [1,2,3,4,5]
new_list = [square**2 for square in list_data]
print(new_list)

string = "Hi I'm Madhavan"
name  = [ i for i in string if i.lower() in "aeiou"]
print(name)


Nested for loop linked comprehension 

a1 = ["sun","mon","tue"]
a2 = ["sunday","thursday","monday","tuesday","friday"]

days = [j for i in a1 for j in a2 if i in j]
print(days)


odd_even = [str(i) + " : Even "if i % 2 == 0 else str(i) + " : Odd "for i in range(1,11)]
print(odd_even)


lis = [ [i for j in range(5)]for i in range(5)]
print(lis)

lis = [ [j for j in range(5)]for i in range(5)]
print(lis)

jump statements
for i in range(1,10):
    if i == 5:
        continue
    print(i,end = " ")

loop else clause

for i in range(0,10):
    print(i,sep = ',',end = " ")
else:
    print("Else clause executed")

for i in range(0,10):
    if i ==5:
        break
    print(i,sep = ',',end = " ")
else:
    print("Else clause not executed")


nums = [11,12,11,14,11]  #hee we write else loop for for statement not for statement

for num in nums:
    if num % 5 == 0:
        print(num)
else:
    print("not found")


list = [1,2,3,5]
list.insert(3,4)
print(list)


list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

list1.append([6,7,8,9,10]) #differance between append and extend
list2.extend([6,7,8,9,10])

print(list1)
print(list2)

list = [1,2,3,4,5]
mis_ele = list.pop(3)
print("Pop function returns the value : ",mis_ele) 


list = [1,2,3,4,5]
list.sort(reverse = True)
print(list)

a = 'Madhavan'
lis = list(a)
print(lis)

for i in lis:
    if  i == 'v':
        break
    print(i)

print("tuple")
a = (1,2,3,4,5)
print(a[4])


na = 'Madhav'
name = tuple(na)
print(name)

lists = tuple([1,2,3,4]) # list inside tuple
print(type(lists))

tup = (1)
print(type(tup))

tupl = (1,)
print(type(tupl))


name = 'Madhavan'
print(name[0:9:2])

name = 'Madhavan'
print(name[10:0:-1])

name = 'Madhavan'
inpt = name[10:0:-1]
print(name) #here the orginal value doesn't change anything
print(inpt)

name = "coding made fun"
outp = name.split() #default is , so it seprates by , 
print(outp)

name = "      coding made fun          "
print(name.strip())

name = "      coding made fun          uhhh"
print(name.lstrip()) #lstrip for left

name = "coding made fun   uhhh       "
print(name.rstrip()) #rstripm for right


name = "Madhav made coding fun" #here we can use lsrtip() and rstrip alsoooooo
print(name.strip('made coding fun')) #strip has been used to remove characgers also


main = 'Madhav made code easy'
sub = 'code'
print(main.find(sub))

main = 'Madhav made code easy'
sub = 'code'
print(main.find(sub,1,20))#here i give a range

main = 'Madhav made code easy'
sub = 'abcd'
print(main.find(sub)) #output will be -1 denotes no value in the given string

name = 'Madhav'
digit  = '12345'
print(name.isdigit())
print(digit.isdigit())

name = 'Madhav'
digit  = '1234 5' # here space consider as character so it shows false
print(name.isdigit())
print(digit.isdigit())

mail = 'Madhavbala07gmailcom'
print(mail.isalnum()) #isalnum means either num or alp

name = "Madhavan bala"
print(name.isspace()) it helps to find the string contains space or not

dic = {1001:'Madhav',1002:'Mathu',1003:'Yazhlini'}
print(dic.keys())

dic = {1001:'Madhav',1002:'Mathu',1003:'Yazhlini'}
print(dic.items()) # to show all the items

dic = {1001:'Madhav',1002:'Mathu',1003:'Yazhlini'}
print(1001 in dic)

dic = {1001:'Madhav',1002:'Mathu',1003:'Yazhlini'}
print('Madhav' in dic.values())

dict1 = {1:'One',2:'Two'}
lis = list(dict1)
print(lis) #it display only keys 

functions
def add():  #function definition
    a = int(input("Enter the value 1 : ")) #it is non-void function because it returns a value
    b = int(input("Enter the value 2 : "))
    return a+ b #return always goes to the function calling 

print(add()) #function calling


def add():  #function definition 
    a = int(input("Enter the value 1 : ")) #it is void function because it doesn't return a value
    b = int(input("Enter the value 2 : "))
    print(a+b)

print(add()) #function calling and it displays none bcz add function doesn't have a return value
#python internally take void function as none value it means the code runs only inside the def function we can't use to another prgrm

def add(a,b):
    return a+b

a = int(input("Enter the value 1 : "))
b = int(input("Enter the value 2 : "))

print(add(a,b))

def exp(exp):
    return (exp)

def name(name):
    return (name)

name = input("Enter the name : ")
exp = int(input("Enter the experiance : "))

# print(f"Hi My name is {name} and have {exp} of experiance ")

def add(a,b):
    return (a+b)

a = int(input("Enter the number 1 : "))
b = int(input("Enter the number 2 : "))

print(add(a,b))
print(add(1,2))

def add(a,b=10): #default parameter value 
    return (a+b)

print(add(7))


def add(a,b=10): #default parameter value 
    return (a+b)

print(add(7,100))

print("oops in pyhton")

class is a design and the object is known as instance(utharnam)
vivo y3 phone is a class and the manufacture area china is a object 
so to create object we need a class(blueprint)

def div(a,b):
    print (a/b)

def smart_div(func):

    def inner(a,b):
        if a < b:
            a,b = b,a
            return func(a,b)
            
    return inner

div = smart_div(div)
div(2,4)


print(div)

class computer:
    attributes --> variables ex:height,age
    behaviour  --> methods[fuctions]

class computer:

    def config(self):
        print("First demo model in oops cocept")

config1 = computer()
print(config1)

class name . method name (object name)
# a proper way to call a methods by using object

class computer:

    def config(self):
        print("second demo model in oops cocept")

config2 = computer()

config2.config() 

__init__ method it means it automatically rin if it is not been called

class madhav():
    def __init__(self):
        print("This is __init__ method")

    def call(self):
        print("This one that I called")
    
obje = madhav()
obje.call()


class computer:
    def __init__(self,model,price):
        self.model = model
        self.price = price


    def info(self):
        print(f"This is {self.model} Brand and the Price is {self.price}")

obje = computer('Vivo',12345)

obje.info()


find a heap memory

class suma:
    pass

obj = suma()
print("To find the Heap memory of the object in computer : ",id(obj)) #$it changes frequently
point to remember everytime we create an object it create a new space and the size of memory based on number of variables

constructor and slef
constructor has been used to calculate the memory and assign a memory 

class employee:
    def __init__(self):
        self.name = 'Madhav'
        self.client = 'AbbVie'

emp1 = employee()
emp2 = employee()

emp2.name='Ashok'
emp2.client='Pfizer'

print(f"Hi, I'm {emp1.name} and I working for {emp1.client} in saama") #it prints the default value assign in the class 
print(f"Hi, I'm {emp2.name} and I working for {emp2.client} in saama") #it prints the modified value given in the object

class employee:
    def __init__(self):
        self.name = 'Madhav'
        self.client = 'AbbVie'

emp1 = employee()
emp2 = employee()

emp2.name='Ashok'
emp2.client='Pfizer'

print(f"Hi, I'm {emp1.name} and I working for {emp1.client} in saama") 
print(f"Hi, I'm {emp2.name} and I working for {emp2.client} in saama") 

                                    class manager:
                                        def __init__(self,employee):
                                            self.employee = employee
                                            

                                        def __init__(self,salary):
                                            self.salary = salary
                                            

                                    emp1 = manager()
                                    emp2 = manager()

                                    emp1.employee = "Maddy"
                                    emp1.salary = 5000000

                                    emp2.employee = "Madhav"
                                    emp2.salary = 10000000

                                    print(f"Hi I'm {emp1.employee} and I receive {emp1.salary} in saama")
                                    print(f"Hi I'm {emp2.employee} and I receive {emp2.salary} in saama")

class Employee():
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary


emp1 = Employee(name = 'Madhav',salary = 646464)
emp2 = Employee(name = "Usain Bolt",salary = 564700)

print(f"Hi I'm {emp1.name} and my salary is {emp1.salary}")
# print(f"Hi I'm {emp2.name} and my salary is {emp2.salary}")


class emp_details:

    def __init__(self):
        self.name =  "Madhav"
        self.age = 21

    # def update(self):
    #     self.age = 30

    def compare(self,other): #compare(who is calling , whom to compare)
        if self.age == other.age:    #it use to compare one function to another
            return True
        else:
            return False

obj1 = emp_details()
obj2 = emp_details()

obj1.age = 20

if obj1.compare(obj2):
    print("The Age is Same")
else:
    print("That's Different")


print("instance variable and , class variable")

class car:

    wheels = 5             #variable declare inside the classs is known as << class >> variable
                                       
    def __init__(self):    # variable declare inside the __init__ function is known as << instance >> variable     
        self.mil = 30
        self.com = " BMW "
        self.price  = " 80L "

obj1 = car()
obj2 = car()

car.wheels = 4                     #it affects all the objects

obj2.com  = " LAMBOGHINI "
obj2.price = " 50L "


print(f"The car company is {obj1.com} this car give {obj1.mil} Mileage and the price if the car is {obj1.price} then it has {car.wheels}  Wheels ")
print(f"The car company is {obj2.com} this car give {obj2.mil} Mileage and the price if the car is {obj2.price} then it has {car.wheels}  Wheels ")



methods in pyhton

class student:

    school = "Sri Ragavendra Matriculation School"


    def __init__(self,tam,eng,mat,sci,soc):
        self.tam = tam
        self.eng = eng
        self.mat = mat
        self.sci = sci
        self.soc = soc 

    def avg(self):
        return (self.tam + self.eng + self.mat + self.sci + self.soc) / 5

Madhavan = student(50,50,50,60,60)
Mathumitha = student(34,34,23,23,21)

print(f"Madhavan Average Mark is {Madhavan.avg()}")
print(f"Madhavan Average Mark is {Mathumitha.avg()}")


Instance has two types 1 -> Accessor methods  2 - > Mutator methods
fetch the value  --> Accessor
modify the value --> Mutator


class student:

    school = "Sri Ragavendra Matriculation School"


    def __init__(self,tam,eng,mat,sci,soc):
        self.tam = tam
        self.eng = eng
        self.mat = mat
        self.sci = sci
        self.soc = soc 

    def avg(self):
        return (self.tam + self.eng + self.mat + self.sci + self.soc) / 5

    def get(self):  #instance for use variable(object) to get value(method)  -- > Accessor
        return self.tam

    def set_tam(self,value):  #here edit the value so --> Mutator
        self.tam = value

Madhavan = student(50,50,50,60,60)
Mathumitha = student(34,34,23,23,21)

print("Def function value taken ",Madhavan.get())
print(Madhavan.set_tam)
print(f"Madhavan Average Mark is {Madhavan.avg()}")
print(f"Madhavan Average Mark is {Mathumitha.avg()}")

class student:

    school = "Sri Ragavendra Matriculation School"
    place = "Sathyamangalam"
    district = "Erode"

    def __init__(self,tam,eng,mat,sci,soc):
        self.tam = tam
        self.eng = eng
        self.mat = mat
        self.sci = sci
        self.soc = soc 

    def avg(self):
        return (self.tam + self.eng + self.mat + self.sci + self.soc) / 5
    
    #to work class object in methods
    def pla(cls):
        return cls.place
    
    def dis(cls) :
        return cls.district
        
    def sch(cls):
        return cls.school

Madhavan = student(50,50,50,60,60)
Mathumitha = student(34,34,23,23,21)

print(f"Madhavan Average Mark is {Madhavan.avg()}")
print(f"Madhavan Average Mark is {Mathumitha.avg()}")

print(Madhavan.sch())
print(Madhavan.pla())
print(Madhavan.dis())


class student:

    school = "Sri Ragavendra Matriculation School"

    def __init__(self,tam,eng,mat,sci,soc):
        self.tam = tam
        self.eng = eng
        self.mat = mat
        self.sci = sci
        self.soc = soc 

    def avg(self):
        return (self.tam + self.eng + self.mat + self.sci + self.soc) / 5
    
    @classmethod       # to tells the compiler it is class set so we can call the method by using class name
    def sch(cls):
        return cls.school

Madhavan = student(50,50,50,60,60)
Mathumitha = student(34,34,23,23,21)

print(student.sch())


class student:

    school = "Sri Ragavendra Matriculation School"

    def __init__(self,tam,eng,mat,sci,soc):
        self.tam = tam
        self.eng = eng
        self.mat = mat
        self.sci = sci
        self.soc = soc 

    def avg(self):
        return (self.tam + self.eng + self.mat + self.sci + self.soc) / 5
    
    @classmethod       # to tells the compiler it is class set so we can call the method by using class name
    def sch(cls):
        return cls.school

    @staticmethod
    def static(): #this static method have no slef so it doesn't mean object or a class
        print("This static used to describe function without class and object(method) to run the method")

Madhavan = student(50,50,50,60,60)
Mathumitha = student(34,34,23,23,21)

print(student.sch())
print(student.static())


print("Inner class in python")
class saama:

    def __init__(self,name,experiance):
        self.name = name
        self.experiance = experiance
        self.client = self.client

    def show(self):
        return (self.name,self.experiance)


    class client:
        def __init__(self):
            self.client = "AbbVie"
            self.salary  = 45678

        def show(self):
            return (self.client,self.salary)

emp1 = saama("Madhav",5)
emp2 = saama("Mathu",3)

seco_class = saama.client()

print(emp1.show())
print(seco_class.show())



print("Single level Inheritance in python")
class employee:
    def __init__(self):
        self.name = "Madhav"
        self.age = 20

    def info(self):
        return ("This method works")

class company(employee):
    def __init__(self):
        self.comp = "Saama"

    def show(self):
        return (f"This employee working in saama")

clascall = employee()
c2 = company()
print(c2.info())


print("Mutilevel Inheritance")
class employee:
    def fearure1(self):
        return ("Feature 1 is working ")

    def feature2(self):
        return ("Feature 2 is working ")

class company(employee):
    def feature3(self):
        return ("Feature 3 is working")

    def feature4(self):
        return ("Feature 4 is working")

class clients(company):

    def feature5(self):
        return ("Feature 5 is working")

    def feature6(self):
        return ("Feature 6 is working")

c1 = clients()

print(c1.feature6())


print("Mutiple Inheritance")
class employee:
    def fearure1(self):
        return ("Feature 1 is working ")

    def feature2(self):
        return ("Feature 2 is working ")

class company(employee):
    def feature3(self):
        return ("Feature 3 is working")

    def feature4(self):
        return ("Feature 4 is working")

class clients(company):

    def feature5(self):
        return ("Feature 5 is working")

    def feature6(self):
        return ("Feature 6 is working")

c1 = clients()

print(c1.feature6()) 

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)
