import random as rd
import time
A=list(['rock','paper','scissor'])
f=rd.choice(A)
u = input("Enter the choice:")
if f == u:
    time.sleep(5)
    print("you win")
else:
    time.sleep(5)
    print("Again try")