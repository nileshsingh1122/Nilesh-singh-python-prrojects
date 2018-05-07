num1=input('enter first number')
num2=input('enter second number')
num3=input('enter third number')
if (num1>=num2)and(num1>=num3):
    largest=num1
elif(num2>=num1)and(num2>=num3):
    largest=num2
else:
    largest=num3
print("the largest number betweenn num1,num2,and num3 is ",largest)  
