s=raw_input()
nl=s.split(" ")
ln=list()
k=0
for x in nl:
    if x=="4":
        k+=1
        nl[nl.index(x)]=""
    else:
        x=int(x)
        ln.append(x)
i=0
ln.sort()
ln.reverse()
while i<len(ln):
    j=i+1
    nl=[i]
    temp=ln[i]
    while j<len(ln):
        temp=temp+ln[j]
        if temp>4:
            temp=ln[i]
            j+=1
            continue
        if temp<=4:
            nl.append(j)
            if temp==4:
                k+=1
                for x in nl:
                    ln[x]=100
                break
        j+=1
    i+=1
nl=list()
for x in ln:
    if x!=100:
        nl.append(x)
c=0
if 1 in nl:
    for x in nl:
        c=1
if 1 not in nl:
    c=len(nl)
k=k+c
print(k)








