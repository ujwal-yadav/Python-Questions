instr="iHi 1there"

def countX(instr, x):
	return instr.count(x)

intMax=0
strMax=0
for i in instr:
    if i.isdigit():
        x=countX(instr, str(i))
        if x>intMax:
            intMax=x;
    if i.isalpha():
        y=countX(instr, str(i))
        if y>strMax:
            strMax=y;

diff=abs(intMax-strMax)
print("diff is ",diff)

temp=instr[diff]
print("Element to remove is ",temp)
if temp!=' ':
    instr=instr.replace(str(temp),'')
instr=instr.replace(' ','$')
print(instr)
