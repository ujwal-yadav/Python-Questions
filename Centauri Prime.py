tc=int(input())
vowels="aeiou"
for i in range(tc):
    kd=input()
    if kd[len(kd)-1] in vowels:
        print(f"Case #{i+1}: {kd} is ruled by Alice.")
    elif kd[len(kd)-1]=="y":
        print(f"Case #{i+1}: {kd} is ruled by nobody.")
    else:
        print(f"Case #{i+1}: {kd} is ruled by Bob.")
