#p(sample_mean(n) + u <= true_mean)<= e^-2nu^2

import random

MEAN = 0.5
u = MEAN/10
n = 100


count = 0
for i in range(100):
    rands = []
    
    for i in range(n):
        rands.append(random.random())
    
    sample_mean = sum(rands)/n
    if sample_mean + u <= MEAN:
        count+=1
prob = count/100


hoeff = 2.71828**(-2*n*(u**2))

print("Upper Bound: ", hoeff)
print("Real Probablity: ",prob)

