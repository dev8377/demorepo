class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)
n1.next=n2
n2.next=n3
n3.next=n4
a=int(input("Enter the data to be deleted: "))
temp=n1
prev=None
if temp and temp.data==a:
    n1=temp.next
else:
    while temp and temp.data != a:
        prev=temp
        temp=temp.next
    if temp:
        prev.next=temp.next
    else:
        print("Data not found")
temp=n1
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("None")