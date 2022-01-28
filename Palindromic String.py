def checkPalin(n):
    r=0
    d=0
    while n>=1:
        r=n%10
        d=r+d*10
        n=n//10
    return d
num="145"
num=int(num)
revNo=checkPalin(num)
while revNo!=num:
    num=num+revNo
    revNo=checkPalin(num)
print("The Palindrome no is ",num)
