"""
Algorithm designed by Izzet Memmedov
Problem : Pay an employee using a gold rod
"""
halqa_sayi=int(input("Input number of rings:"))

kesiyler=[]
n=3
while n<halqa_sayi:
    kesiyler.append(n)
    n=(n+1)*2
kesiy_sayi=len(kesiyler)

print(f"number of cuts:{kesiy_sayi}")
print(f"index of cuts:{kesiyler}")