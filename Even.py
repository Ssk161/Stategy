#Chceking even or odd number
n=int(input())
if(n%2==0):
    print("even")
else:
    print("odd")

#swap values without using 3rd variable
a,b=map(int,input().split())
print("before sorting",a,b)
a=a+b
b=a-b
a=a-b
print("after sorting",a,b)

#pattern programmes
n=int(input())          
for i in range(1,n+1):
    for j in range(0,i):
        print("* ")
    print()



