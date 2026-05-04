class node:
    def __init__(self,data):
        self.pre=None
        self.data=data
        self.next=None
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)
n1.next=n2
n2.pre=n1
n2.next=n3
n3.pre=n2
n3.next=n4
n4.pre=n3
temp=n1
while temp:
    print(temp.data,end="<-->")
    temp=temp.next
print("None")