def checkPalin(num):
    num2=str(num);
    mid=len(num2)//2;
    if len(num2)%2==0:
        if num2[mid]>num2[mid-1]:
            temp=(int(num2)//100)+1;
            temp=temp*100;
            return checkPalin(temp);
        else:
            numleft=num2[:mid]
            nxt=numleft+numleft[::-1]
            return int(nxt)
    else:
        if num2[mid+1]>num2[mid-1]:
            temp=(int(num2)//100)+1;
            temp=temp*100;
            return checkPalin(temp);
        else:
            numleft=num2[:mid]
            nxt=num2[:mid+1]+numleft[::-1]
            return int(nxt);
t=checkPalin(32100);
print(t)
