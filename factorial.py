num = int(input("Enter a number: "))
factorial = 1
if num==0:
	print(1)
elif num == 1:
    print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
        factorial = factorial*i
print(factorial)
