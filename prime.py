lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
c=0
for num in range(lower,upper + 1):

   if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
            	break
        else:
        	c=c+1
           	print(num)
print(c)  
