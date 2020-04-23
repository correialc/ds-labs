from math import pi

def liqvol(h, r=10):
    return (4*pi*(r**3))/3 - (pi*(h**2)*(3*r-h))/3

print(liqvol(2))