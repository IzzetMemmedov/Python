"""
Algorithm designed by Izzet Memmedov
Problem : find Minimum number of change
""" 
x1=int(input("input first change:"))
x2=int(input("input second change:"))
x3=int(input("input third change:"))
if x1>x2 :
    x1,x2=x2,x1
if x2>x3:
    x2,x3=x3,x2
if x1>x2 :
    x1,x2=x2,x1
info=int(input("input your money:"))
f=[0]*info
for i in range(1,info+1):
    if i==x1:
        f[i-1]=1
    else:
        if i<x2:
            if (i//x1)*x1==i:
                f[i-1]=i//x1
        else:
            if i==x2:
                f[i-1]=1
            if i<x3:
                if f[i-1-x1]!=0:
                    f[i-1]=f[i-1-x1]+1
                if f[i-1-x2]!=0:
                    f[i-1]= min(f[i-1],f[i-1-x2]+1)
            else:
                if i==x3:
                    f[i-1]=1
                else:
                    f[i-1]=0
                    if f[i-1-x1]!=0:
                        f[i-1]=f[i-1-x1]+1
                    if f[i-1-x2]!=0:
                        f[i-1]= min(f[i-1],f[i-1-x2]+1)
                    if f[i-1-x3]!=0:
                        f[i-1]=min(f[i-1],f[i-1-x3]+1)


if f[info-1]!=0:
    print(f"answer {f[info-1]}")
else:
    print("imposible.")


