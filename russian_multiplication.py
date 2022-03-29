def rus_mul(a,b):
    s=0
    while(a!=0 and b!=0):
        if(a%2!=0):
            s=s+b
        a=a//2
        b=b*2
    return(s)

a,b=map(int,input().split())
print(rus_mul(a,b))
        
