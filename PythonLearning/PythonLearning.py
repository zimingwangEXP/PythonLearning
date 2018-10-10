import random
a=[random.randint(1,1000) for i in range(0,20)]
print(a)
a[::2]=sorted(a[::2],reverse =True)
print(a)