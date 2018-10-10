isPrime=[True for i in range(0,1000)]
Prime=[]
#欧拉
def GetPrime(a):
    for  i in range(2,a):
        if(isPrime[i]):Prime.append(i)
        for p in Prime:
            if(p*i>=1000):break
            isPrime[p*i]=False
            if(i%p==0):break;
ans=[]
inp=int(input("请输入一个小于1000的正整数\n"))
assert(0<inp<1000,"输入的有误，请重试")
GetPrime(inp);
for p in Prime:
    while(inp%p==0):
        inp/=p;
        ans.append(str(p));
print('X'.join(ans))