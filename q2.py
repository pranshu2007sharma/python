a=int(input("Enter a number to be proven to be prime"))
f= False
if a==1 or a==0:
   print(a,"is not a prime number")
else:
   for i in range(2,a):
      if(a%i)==0:
         f= True
         break
if f:
   print(a,"is not a prime number")
else:
   print(a, "is a prime number")