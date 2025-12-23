num=int(input("Enter the integer: "))

if num%2==0:
    print("Even number")
else:
    print("Odd number")



num=int(input("Enter the number: "))

if num>0:
    print("Pos Num")
elif num==0:
    print("Zero")
else:
    print("Neg Num")


age = int(input("Enter the age: "))
if age>=18:
    print("Eligible to Vote")

num1= int(input())
num2= int(input())

if num1>num2:
    print(num1)
else:
    print(num2)



a=int(input())
b=int(input())
c=int(input())

if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)


if a>b:
    if a>c:
        print(a)
    else:
        print(c)

else:
    if b>c:
        print(b)
    else:
        print(c)



mark= int(input())

if mark>=90:
    print("A")
elif mark>=75:
    print("B")
elif mark>=50:
    print("C")
else:
    print("Fail")


su='admin'
sp='1234'

username= input()
pwd= input()

if username == su:
    if pwd==sp:
        print("Lo Su")
    else:
        print("Inc Pwd")
else:
    print("Inv Un")



n= int(input())

if 1<= n <=10 :
    print("Btw 1 - 10")
elif 11<=n <=20:
    print("Btw 11- 20")
elif n>20:
    print(">20")



a= int(input())
b=int(input())
ch=input()

if ch=='+':
    print(a+b)
elif ch=='-':
    print(a-b)
elif ch=='*':
    print(a*b)
elif ch=='/':
    print(a/b)


mark= int(input())
if marks>40:
    print("Pass")
else:
    print("Fail")
    '''
