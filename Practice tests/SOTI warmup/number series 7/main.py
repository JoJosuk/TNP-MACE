t=int(input())
for i in range(t):
    n=int(input())
    if(n==1):
        print("1 1")
    else:
        lis=[]
        for i in range(1,n-1):
            lis.append(i)
        j=n-1
        for i in range(2):
            lis.append(j)
        s=2**n-sum(lis)
        lis.append(s)
        print(" ".join(map(str,lis)))
        
