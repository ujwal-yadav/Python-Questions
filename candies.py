tc=int(input())

for i in range(tc):
    b,k=input().split(" ")
    arr=list(map(int,input().split(" ")))
    s=sum(arr)
    print(f"Case #{i+1}: {s%int(k)}")
