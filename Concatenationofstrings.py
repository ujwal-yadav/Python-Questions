s="3,2,6,5,1,4,8,9"
s=s.split(",")
num1=0
num2=""
i=0;
while i<len(s) :
    if(s[i]=="5"):
        while(s[i]!="8"):
            num2=num2+s[i]
            i=i+1;
        if(s[i]=="8"):
            num2=num2+s[i]
            i=i+1;
    else:
        num1=num1+int(s[i])
        i=i+1;
print("num1 is : ",num1)
print("num2 is : ",num2)
print("Sum of num1 and num2 is : ",num1+int(num2))
