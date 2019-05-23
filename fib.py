import math

n = int(input('enter nth position: '))

phi = (1+math.sqrt(5))/2 # golden mean
psi = (1-math.sqrt(5))/2 # golden number

# using Binet's equation
an = (phi**n-psi**n)/math.sqrt(5) 

print(int(an))

