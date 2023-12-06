def sum_div(n):
    s,k=1,2
    while (k*k<=n):
        if n%k==0:
            s=s+k
            m=n//k
            if m != k:
                s=s+m
        k=k+1        
    return s  
 
def  is_friend(n1,n2):
    return (sum_div(n1)==n2) and (sum_div(n2)==n1)
 
def task(n):
    for i in range(2,n+1):
        q=sum_div(i)
        if (q>i) and sum_div(q)==i:
            print(i,q)
 
task(20000)