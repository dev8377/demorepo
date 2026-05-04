a=[5,8,7,6]  #size
b=[2.5,3.0,2.0,2.2]  #cost
c=0
for i in range(len(a)):
    if a[i]>a[c] or a[i]==a[c] and b[i]<b[c]:
        c=i
print("The best pine apple is of cost ",b[c])
print("The best pine apple is of size: ",a[c])