s ="3,2,6,5,1,4,8,9"

array = list(map(int,s.split(",")))
num1=sum(array[:array.index(5)]+array[array.index(8)+1:])
print("num1 is :",num1)

num2=""
st = array[array.index(5):array.index(8) + 1]
for i in st:
    num2=num2+str(i)

print("num2 is :",num2)
print("Sum of num1 and num2 is : ",num1+int(num2))
