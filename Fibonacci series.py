terms = int(input("Enter Terms : "))
a, b = 0, 1
count = 0

if terms <= 0:
   print("Please enter a positive integer")

elif terms == 1:
   print("Fibonacci sequence upto",terms,":")
   print(a)

else:
   while count < terms:
       print(a)
       nth = a + b
       a = b
       b = nth
       count += 1
