num=int(input("Enter the Number: "))
fact=1
for i in range (1,num+1):
    fact*=i
print(f"Factorial of {num} is {fact}")