a=[3,5,3,10,62,23,6,34,94,2,9,47,46,5]
n=8
x=min(a)
print(x)
i=0
r=[]
print("Value of a before",a)
while(i<len(a)):
    if a[a.index(x)+1]>n:
        r.append(n)
        print("@@@@")
        
    elif x>a[i] and a[i+1]>n:
        x=a[i]

        print(i)
        r.append(n)
    else:
        print("2",i)
        r.append(a[i])
    i+=1
print("Value of a after",a)    
