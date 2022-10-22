"""
Algorithm designed by Izzet Memmedov
Problem : Longest Increasing Subsequence
"""
say=int(input("input lenght of your list:"))
elementler=[]
cvb_list=[0]*say
cvb_list[0]=1
max=1
max_list=[]
for i in range(say):
    n=int(input(f"{i+1}th element:"))
    elementler.append(n)
for i in range(1,say):
    cvb_list[i]=1
    for j in range(i):
        if elementler[j]<elementler[i] and cvb_list[i]<cvb_list[j]+1:
            cvb_list[i]=cvb_list[j]+1
        if cvb_list[i]>max:
            maxindex=i
            max=cvb_list[i]
max_list.append(elementler[maxindex])
max=maxindex
for i in range(maxindex-1,-1,-1):
    if cvb_list[i]+1==cvb_list[max] and elementler[i]<elementler[max]:
        max_list.append(elementler[i])
        max=i
max_list.sort()
print(f"number of elements:{cvb_list[maxindex]}")
print(f"list:{max_list}")

            
