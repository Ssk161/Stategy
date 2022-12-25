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



