import math

def Suma(a,b):
    real=a[0]+b[0]
    imag=a[1]+b[1]
    return(real,imag)

def Resta(a,b):
    realr=a[0]-b[0]
    imagr=a[1]-b[1]
    return(realr,imagr)

def Producto(a,b):
    producent=(a[0]*b[0]+(a[1]*b[1])*-1)
    producima=(a[0]*b[1]+a[1]*b[0])
    return (producent,producima)

def Division(a,b):
    c=Conjugado(b)
    numerador=Producto(a,c)
    denominador=Producto(b,c)
    return((numerador[0]/denominador[0]),(numerador[1]/denominador[0]))

def Modulo(a):
    modl=math.sqrt((a[0]*a[0])+(a[1]*a[1]))
    return modl

def Conjugado(a):
    d=a[1]*-1
    return(a[0],d)

def ConversionPolarACartesiana(r,alf):
    x=r*(math.cos(math.radians(alf)))
    y=r*(math.sin(math.radians(alf)))
    return (x,y)

def ConversionCartesianaAPolar(x,y):
    r=math.sqrt((x*x)+(y*y))
    alfa=math.degrees(math.atan(y/x))
    return (r,alfa)

def Fase(a):
    fase=math.degrees(math.atan(a[1]/a[0]))
    return fase
if __name__ == '__main__':
    print(Suma((5, 6), (25, 9)))