#stack 
a=[]
n=int(input("Enter the no of elements: "))
for i in range(n):
    b=int(input("Enter the element: "))
    a.append(b) # pushing the element
print("Before popping")
print(a)
a.pop()
print("After popping")
print(a)

#queue
from collections import deque
a=deque()
n=int(input("Enter the no of elements "))
for i in range(n):
    b=int(input("Enter the value: "))
    a.append(b)
print("Before poping ",a)
a.popleft()
print("After poping",a)