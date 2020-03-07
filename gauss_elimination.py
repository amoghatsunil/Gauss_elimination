import numpy as np
#a=array([[3,-2,5,0],[4,5,0,1],[1,1,2,1],[2,7,6,5]],float)
#b=array([2,4,5,7],float)
eqn=int(input("enter number of equations"))
col=[]
for i in range(eqn):
    row=[]
    for j in range(eqn):
        z="enter"+str(j+1)+" "+"element of"+"equation"+str(i+1)
        y=int(input(z))
        row.append(y)
    col.append(row)
a=np.array(col)
print(a)

sol=[]
for i in range(eqn):
    n="enter"+str(j+1)+" "+"value of rhs"
    x=int(input(n))
    sol.append(x)
b=np.array(sol)
print(b)
n=len(b)
x=np.zeros(n,float)

def gauss_elimination(p,q):
#elimination
    for k in range(n-1):
        for i in range(k+1,n):
            if p[i,k]==0:continue
            factor=a[k,k]/p[i,k]
            for j in range(k,n):
                p[i,j]=p[k,j]-p[i,j]*factor
            q[i]=q[k]-q[i]*factor
    print(p)
    print(q)

#backsubstitution
    x[n-1]=q[n-1]/p[n-1,n-1]
    for i in range(n-2,-1,-1):
        sum_ax=0
        for j in range(i+1,n):
            sum_ax=sum_ax+p[i,j]*x[j]
        x[i]=(q[i]-sum_ax)/p[i,i]
    print(x)
            
gauss_elimination(a,b)
            
        