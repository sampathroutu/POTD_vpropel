s1=raw_input()
s2=raw_input()
n=int(input())
s=list()
s.append(s1)
s.append(s2)
j=0
while j<n-2:
    i=0
    ln=""
    while i<len(s[j]):
        if i%2==0:
            t=ord(s[j][i])
            t+=1
            if t==123:
                t=97
            ch=chr(t)
            ln=ln+ch
        elif i%2!=0:
            t=ord(s[j+1][i])
            t+=1
            if t==123:
                t=97
            ch=chr(t)
            ln=ln+ch
        i+=1
    s.append(ln)
    j+=1
print(s[n-1])



