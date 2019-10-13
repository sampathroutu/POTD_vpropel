n=int(input())
i=0
ln=list()
nl=list()
rat=[]
while i<n:
    temp=list()
    for x in range(n):
        g=raw_input()
        temp.append(g)
    if i==0:
        for x in temp:
            ln.append(x)
    elif i==n-1:
        temp.reverse()
        for x in temp:
            ln.append(x)
    else:
        var=list()
        x=temp.pop(0)
        y=temp.pop(len(temp)-2)
        ln.append(y)
        nl.append(x)
        for x in temp:
            var.append(x)
        rat.append(var)
    i+=1
i=2
nl.reverse()
for x in nl:
    ln.append(x)
while i<len(ln):
    temp=ln[i-2]
    ln[i-2]=ln[i]
    ln[i]=temp
    i+=2
i=0
k=0
c=len(ln)-1
t2=list()
while i<n:
    t1=list()
    if i==0:
        j=0
        while j<n:
            t1.append(ln[j])
            j+=1
        t2.append(t1)
    elif i==n-1:
        j=len(ln)-len(nl)-1
        while j>len(ln)-len(nl)-n-1:
            t1.append(ln[j])
            j-=1
        t2.append(t1)
    else:
        t1.append(ln[c])
        z=0
        while z<len(rat):
            t1.append(rat[k][z])
            z+=1
        t1.append(ln[n-1+i])
        k+=1
        c-=1
        t2.append(t1)
    i+=1
for y in t2:
    temp=""
    for x in y:
        temp=temp+x+"\t"
    print(temp)
