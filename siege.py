import math
from fractions import Fraction

fov = float(input("FOV="))
coef = float(input("Coefficient="))

if coef > 0:
    acog = math.atan(coef*math.tan(math.radians(fov)/2*0.35))/math.atan(coef*math.tan(math.radians(fov)/2))/0.35
    iron = math.atan(coef*math.tan(math.radians(fov)/2*0.9))/math.atan(coef*math.tan(math.radians(fov)/2))/0.6
else:
    acog = math.tan(math.radians(fov)/2*0.35)/math.tan(math.radians(fov)/2)/0.35
    iron = math.tan(math.radians(fov)/2*0.9)/math.tan(math.radians(fov)/2)/.6

approximations = str(Fraction(acog/iron).limit_denominator(100)).split('/')

approximations = [int(a) for a in approximations]

XFactor = acog / approximations[0]

output = '\nACOG ADS Sensitivity: {}\nIronsight ADS Sensitivity: {}'.format(approximations[0], approximations[1])

output += '\nXFactorAiming={:.6f}'.format(XFactor)

print(output)
