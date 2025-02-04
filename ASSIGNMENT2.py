list1=[10,20,30,40,50,60,70,80]
list1.append(200)
list1.append(300)

print(list1)

list1.remove(10)
list1.remove(30)

list1.sort()

print(list1)

list1.sort(reverse=True)

print(list1)

tuple1=(45, 89.5, 76, 45.4, 89, 92, 58, 45)

maxmarks=max(tuple1)
indexmax=tuple1.index(maxmarks)
print("Maximum Marks:",maxmarks)
print("Index of Maximum Marks:",indexmax)
minmarks=min(tuple1)
freq=tuple1.count(minmarks)
print("Minimum Marks:",minmarks)
print("Frequency of Minimum Marks:",freq)
list1=list(reversed(tuple1))
print("Reversed Tuple:",list1)

marks=int(input("Enter the marks:"))
if marks in tuple1:
    print("Marks is present in the tuple")
    print("Frequency of Marks:",tuple1.index(marks)+1)
else:
    print("Marks is not present in the tuple")

import random
list100=[]
for i in range(1,101):
    list100.append(random.randint(100,900))
print("List of 100 Random Numbers:",list100)

def count(list100):
    even=[]
    odd=[]
    for i in list100:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
def prime(list100):
    prime=[]
    for i in list100:
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                prime.append(i)
    return prime

even,odd=count(list100)
print("Number of Even Numbers:",even)
print("Number of Odd Numbers:",odd)
prime=prime(list100)
print("Number of Prime Numbers:",prime)


a={34, 56, 78, 90}
b={78, 45, 90, 23}
c=a.union(b)
d=a.intersection(b)
e=c.difference(d)
print("Union of Sets:",c)
print("Intersection of Sets:",d)
print("Difference of Sets:",e)
print("Symmetric Difference of Sets:",a.symmetric_difference(b))
print("Subset of Sets:",a.issubset(b))
print("Superset of Sets:",a.issuperset(b))

n=int(input("Enter element:"))
if n in a:
    print("Element is present in the set")
else:
    print("Element is not present in the set")

dict1={
    "Name":"John",
    "Age":25,
    "salary":25000,
    "city":"New York"
}

dict1["Age"]=26
dict1["city"]="California"
print("Updated Dictionary:",dict1)