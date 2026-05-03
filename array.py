#traversal
n=int(input("Enter the no of elements: "))
arr=[]
for i in range(n):
    a=int(input("Enter the elements: "))
    arr.append(a)
print("Array elements: ")
for i in arr:
    print(i,end=" ")

#insertion
value=int(input("\nEnter the element to be inserted: "))
pos=int(input("Enter the positions to insert the element: "))
arr.insert(pos,value)
print("Array after insertion ")
for i in arr:
    print(i,end=" ")

#Deletion by value
d=int(input("\nEnter the value to be deleted: "))
arr.remove(d)
print("Array after deletion")
for i in arr:
    print(i,end=" ")

#deletion by index or position
d=int(input("\nEnter the position(index) of element to be deleted: "))
for i in range(len(arr)):
    if i==d:
        arr.pop(d)
print("Array after deletion ")
for i in arr:
    print(i,end=" ")
