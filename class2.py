import math
# get the value of principal(p) from the user

X = input("Put a number")

x = int(X)
P = int(input("Tell me the value of p "))
#get the value of R(Rate)
R = float(input("Tell me the value of RATE "))
#get the value of t(time)
T = float(input("Tell me the value of TIME "))
#calculate it
S = P*R*T/100
#print out the result
print("The simple interest is ", S)
