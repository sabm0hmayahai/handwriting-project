import numpy as np
import matplotlib.pyplot as plt


'''c is the value of the baseline a.k.a. the distance between the two transducers/ultrasonic sensors'''

#c = 80

print("start to run\n")
'''z=np.genfromtxt("C:\\Users\\mukhe\\Desktop\\nmit hacks\\data_session3.txt", unpack=True)
length = len(z)

print(z)

for q in range(0,length-1):
    a,b = z[q].split(",")

print(a)
print(b)
'''



file = open("C:\\Users\\mukhe\\Desktop\\nmit hacks\\data_session9.txt","r")

a = []
b = []

for line in file:
    p,q = line.split(",")
    p = int(p)
    q = int(q)
    a.append(p)
    b.append(q)   

'''
x = []
y = []

for i,j in zip(a,b):
    p = ( (c*c) + (j*j) - (i*i)) / (2*c)
    x.append(p)
    q =  ( (j*j) - (p*p)) ** 0.5
    y.append(q)
    
    print("x: ",i)
    print("\n")
    print("y: ",j)
    print("\n")'''
plt.plot(a,b)
plt.show()

#plt.savefig("C:\\Users\\mukhe\\Desktop\\nmit hacks\\data_session2.pdf")

print("end of run\n")
