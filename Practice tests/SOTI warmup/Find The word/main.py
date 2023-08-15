max_len=0
pos=0
count=0
k=input()
subs=[]
n=len(k)
for i in range(1,n+1):
    for beg in range(n-i+1):
        end=i+beg
        sub=k[beg:end]
        subs.append(sub)
for i in subs:
    if i==i[::-1] and len(i)>max_len:
        max_len=len(i)
        pos=i
print(pos)