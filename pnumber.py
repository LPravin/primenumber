import math

for i in range(2,101):
    f=0
    t=int(math.sqrt(i)+1)
    for j in range(2,t):
        if i%j==0:
        	f=1
        	break
    if f!=1:
        print(i)
        