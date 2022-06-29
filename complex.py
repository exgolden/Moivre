import numpy as np
print("Calculadora de las n-esimas raices de un numero complejo")
a=float(input("Parte real: "))
b=float(input("Parte imaginaria: "))
n=int(input("Raiz n: "))
z=complex(a, b)
w=np.arctan(abs(b)/abs(a))
r=abs(z)
if(a>=0 and b>=0):
    theta=w
elif(a<=0 and b>=0):
    theta=w+np.pi
elif(a>=0 and b<=0):
    theta=-w
elif(a<=0 and b>=0):
    theta=np.pi-w
def moivre(n, r, theta, k):   
    x=r**(1/n)*complex((np.cos((theta+2*k*np.pi)/n)), 
                       (np.sin((theta+2*k*np.pi)/n)))
    print(x)
for i in range(0, n):
    moivre(n, r, theta, i)