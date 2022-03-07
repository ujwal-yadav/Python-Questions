num="3456"
otp=""
for i in range(len(num)):
    if i%2!=0:
        otp=otp+str(int(num[i])**2)
otp=otp[:4]
print(otp)
