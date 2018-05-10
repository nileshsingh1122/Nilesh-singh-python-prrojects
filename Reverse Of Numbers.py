n=int(input("Enter number: "))
rev=0
while(n>0):
    fin=n%10
    rev=rev*10+fin
    n=n//10
print("reverse of the number:",rev)
