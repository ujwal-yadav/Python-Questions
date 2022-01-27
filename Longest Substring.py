s = str("ABCADE")
l=[]
i = 0
lenn=0
for j in range(len(s)*2):
    if(i >= len(s)):
        lenn=max(len(l),lenn)
        break
    if s[i] not in l:
        l.append(s[i])
        i+=1
    else:
        i=s.index(s[i])+1
        j=i
        lenn=max(len(l),lenn)
        l.clear()
print("length is ",lenn)
