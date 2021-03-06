import matplotlib.pyplot as plt
import sys,re,time
from sympy import *

if len(sys.argv) == 5:
	Third = sys.argv[1]
	Second = sys.argv[2]
	First = sys.argv[3]
	Constant = sys.argv[4]
else:
	print "Not enough arguments\n"

def plot(third,second,first,constant,pointX):
	a=[]
	b=[]
	for x in range(-1000,1000,1):
		y=int(third)*x**3+int(second)*x**2+int(first)*x+int(constant)
		a.append(x)
		b.append(y)

	#fig = plt.figure()
	#axes = fig.add_subplot(111)
	#axes.plot(a,b)

	plt.plot(a,b)


	pointY=int(third)*pointX**3+int(second)*pointX**2+int(first)*pointX+int(constant)
	plt.annotate('Local Minimum', xy=(pointX, pointY), xytext=(pointX,pointY), arrowprops=dict(facecolor='black', shrink=0.05),) 
	print("\tY:%f" %pointY );
	plt.ylim(-50,50)
	plt.xlim(-50,50)
	plt.show()

#main
x=Symbol('x')
f=Function('f')(x)

cur_x = 1 # Start of algorithm
gamma = 0.01 # step size multiplier
precision = 0.00001 #approach a derivative of 0
noise = 0 #noise factor
previous_step_size = cur_x


expression = (int(Third) * x**3) + (int(Second) * x**2) + (int(First) * x) + int(Constant) 
df=lambdify(x,diff(expression,x)+noise,"numpy")

step=0
while previous_step_size > precision:
    step += 1
    prev_x = cur_x
    cur_x += -gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    print("Step:%i\tX:%f\tDerivative:%f" %(step,cur_x,df(cur_x)))
 
print("\nLocal Minimum:\n\tDerivative:%f\n\tPrecision:%f\n\tNoise:%f\n\tX:%f" % (df(cur_x),precision,noise,cur_x))
plot(Third,Second,First,Constant,cur_x)

