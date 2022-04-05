dx=0.000001
def fx(x):
    return pow(x,pow(x,pow(x,x)))
fprimex=(fx(2+dx)-fx(2))/dx
print(fprimex)
