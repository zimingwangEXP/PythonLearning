print([i for i in range(1,1000) if  i==sum( [k for k in range(1,i) if i%k==0])])
