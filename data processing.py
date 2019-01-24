import numpy as np
import matplotlib.pyplot as plt


print("start processing . . .\n")

'''file will get two coordinate values seperated by a comma'''

file = open("/Users/hegderajesh/Desktop/demo/demo.txt","r")

a = []
b = []

'''the above mentioned comma is removed by using the split() function and then storing
the individual x and y coordinates in the list a and b seperately after
coverting it into integer'''

for line in file:
    p,q = line.split(",")
    p = int(p)
    q = int(q)
    a.append(-p)
    b.append(q)

gh=[0,0,0,-80]
hg=[0,80,0,0]
plt.plot(gh,hg)
plt.plot(a,b)

plt.show()

''' -p is stored in a because our origin is from the right
unlike the common standard(from the left) supported
by the matplotlib'''


x = a
y = b


'''check if the x is staying sort of constant
for that take average of a calculated alpha(assumed) values and check if
the average is below a set tolerance level'''

length = len(x)

nx = []
ny = []
k = 0

'''alpha  tolerance is a key component in the vertical analysis'''
alpha = 15

tolerance = 2
for i in range(0,length-(alpha+1),alpha):
    s = 0
    for j in range(i,i+alpha):
        s = s + x[j]
    avg = s/alpha
    s = 0
    for j in range(i,i+alpha):
        s = s + abs(avg - x[j])
    avg_std_x = s/20
    #print("average standard deviation of x is: ",avg_std_x)
    if(avg_std_x < tolerance): #if the deviation from mean indicates a vertical line
        nx.append(x[i])
        ny.append(y[i])
        nx.append(x[i+alpha])
        ny.append(y[i+alpha])
    else:
        for j in range(i-4,i+(alpha-4)): #if the deviation from mean indicates a non vertical or horizontal line
            nx.append((x[j-4]+x[j-3]+x[j-2]+x[j-1]+x[j]+x[j+1]+x[j+2]+x[j+3]+x[j+4])/9)
            ny.append((y[j-4]+y[j-3]+y[j-2]+y[j-1]+y[j]+y[j+1]+y[j+2]+y[j+3]+y[j+4])/9)
        
    #print("i= ",i)


length = len(nx)
'''the average of 4 neighbours is taken for each value of a and b
and the coordinate value is stored in lists x and y seperately'''




#for i,j in zip(a,b):

'''will create a plot that with x and y values'''
gh=[0,0,0,-80]
hg=[0,80,0,0]
plt.plot(gh,hg)
plt.plot(nx,ny)

'''will show the plot, similar to the imshow function in opencv'''
plt.show()

gh=[0,0,0,-80]
hg=[0,80,0,0]
plt.plot(gh,hg)
plt.plot(nx,ny)


'''if enabled, the command will save a pdf of the plotted figure'''
'''NOTE: only enable ONE of plt.show() or plt.savefig() at a time
i.e. either show or save figure'''
print("Successfully processed data session\n")
print("\nPDF created\n")
print("\nUploading to cloud . . . \n")

plt.savefig("/Users/hegderajesh/Desktop/demo/demo.pdf")


print("end of run\n")
