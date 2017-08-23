import numpy
w1 = numpy.random.randn()
w2 = numpy.random.randn()
def NN(m1,m2,w1,w2,b):
    def cost(b):
        if(m1>m2):
            return (b-m1)**2
        else:
            return (b-m2)**2
    def num_slope(b):
        h=0.00001
        return(cost(b+h)-cost(b))/h
    def slope(b):
        if(m1>m2):
            return num_slope(b)*(b-m1)
        else:
            return num_slope(b)*(b-m2)
    b = b-0.1*slope(b)
    z = m1*w1 + m2*w2 + b
    identifier = sigmoid(z) 
    if(identifier>=0.9):
        print("its a Bomber/Logical True")
    else:
        print("its a Fighter/Logical False")
def sigmoid(x):
    return 1/(1+numpy.exp(-x))
m1 = input("Enter value for 1st Input")
m2 = input("Enter value for 2nd Input")
NN(float(m1),float(m2),w1,w2,5)
