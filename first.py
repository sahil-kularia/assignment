here i am writing the 16 basic code that are necessary for learning python # type: ignore

print('hello world')

for i in range(0,3):
    print('sahil')

a = "sahil"
b = ' kularia'
c = a+b
print(c)

a = 12
b = 12
c = a+b
d= a+2*b-12*2
print(c,d)

a = "sahil"
b = 12
c = a+str(b)
print(c)

a = 12
b = 1
c = 2
d = a+b+c
e = a-b+c
print(d)
print(e)

a = "good"
b = " morning "
c = input('enter your name here')
print(a+b+c)

i = int(input('enter the first number'))
j = int(input('enter the second number'))
k = i+j
print(k)

i = 1
while (i<5):
    print('hi')
    i=i+1

range can  be printed using the word list and also range is always in increasing order # type: ignore
print("range of (-1,-5) is --> ",list(range(-5,-1)))

for i in range(0,-10,-4):
    print(i)

for i in range(1,11):
    print("4*",i,"=",4*i)

sum = 0
for i in range(0,11):
    sum = sum+i
print(sum)

i = 1
while (i<=10):
    print("7*",i,"=",7*i)
    i=i+1

for i in range(1,11):
    print("9 * ",i,"=",9*i)

i = int(input('enter the number whose table is required : '))
for t in range(1,11):
    print(i,'*',t,'=',i*t)

p = int(input('enter the number till whose sum is required'))
sum  = 0
for i in range(1,p+1) :
    sum = sum+i
print(sum)

marks = int(input('enter the marks '))
if (marks>90):
    print('excellent')
elif(marks>75 and marks<90):
    print('good')
elif(marks>45 and marks<75):
    print('average')
else:
    print('failed')

a = int(input('enter the first number here :'))
b = int(input('enter the second number : '))
if (a>b):
    print('a is greater than b by : ',a-b)
elif(b>a):
     print('b is greater than a by : ',-(a-b))
else:
    print('both number are same')

a = int(input('enter the number here '))
if(a%2==0):
    print('number is even')
else:
    print('number is odd')

a = int(input('enter the number here : '))
for i in range(2,a):
    if(a%i==0):
        print('number is composite')
        break
else:
    print('number is prime')
    

a = input('enter the first word')
b = input('enter the second number')
if a==b:
    print("a==b")
elif(a>b):
    print("a>b")
else:
    print("b>a")

p=[]
for i in range(1,4):
     num = int(input('enter the number '))
     p.append(num)

maxed = max(p)
print(maxed)

n = int(input('enter the number here'))
sum = 0
for i in range(1,n+1):
    if(i%7==0 and i%9==0):
        sum=sum+i
print('total sum is : ',sum)

n = int(input('enter the number here : '))
sum = 0
for i in range(2,n+1):
    if(n%i!=0):
        sum=sum+i
print('total sum of prime number is : ',sum)

def add(a,b):
    c=a+b
    print(c)

add(3,7)
add('sahil',"kularia")

def prime(a):
    for i in range(2,a):
        if(a%i==0):
            print('composite number')
            break
    else:
        print('prime number')

prime(4)
prime(7)
prime(12)
prime(15)
prime(77)
prime(111)
prime(199)

def sum(a):
    n = 0
    for i in range(1,a+1):
        n = n+i
    print('total sum of number ',a,"is ",n)

sum(3)
sum(5)
sum(10)

# 5-->1+3+5
def odd():
    n = int(input('enter the number here: '))
    sum = 0
    for i in range(1,n+1):
        if(i%2!=0):
            sum=sum+i
    print('total sum of odd number in ',n,"is",sum)

odd()

def prime():
    n = int(input('enter the number here'))
    sum = 0
    for i in (2,n):
        if(n%i!=0):
            sum=sum+i
    print('total sum of prime number is : ',sum+n)

prime()

# string and its indexing as well as slicling
t ="HEllO world"
print(t)
print(t[0:])
print(t[0:4])
print(t[0:5])
print(t[0:6])
print(t[0:46])
print(t[4:])
print(t[6:10])
print(len(t))
print(t.upper())
print(t.lower())

name = input('enter your name here')
age = int(input('enter your age here '))
price = float(input('enter your price your'))
print('my name is ',name.upper(),'and age is',age,'and the price of this product is ',price)

# string.strip is used to remove the unnecessary spaces 

string = 'indian    army    '
print(string)
print(len(string))
string.strip()
print(len(string))
print(string[::1])
print(string[::-2])

# mathematics python in use
import math as mm
print(mm.exp(11))
print(mm.log(20,2))
print(mm.cos(45))
print(mm.tan(90))
print(mm.ceil(4.34343))

# palidrom
# it is defined as if our text is same from the start as well as end
s1="indian"
s2='madam'
print(s1==s1[::-1])
print(s2==s2[::-1])

# randow number generator 
import random as r
print(r.random())
# random int number generated
print(r.randint(1,10))
print(r.randint(11,99))

# select random sample from the given sample provided
a=[11,45,23,90,55,12]
print(r.sample(a,4))
print(r.sample(range(51,61),3))

# generate random string
import string as s
import random as r

print(s.ascii_letters)
print()
