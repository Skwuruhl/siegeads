import math
from fractions import Fraction

fov = float(input("FOV="))
mode = input("Mode ('zoom' or 'monitor distance')=")
coef = float(input("Coefficient="))

if mode == 'zoom':
    acog = math.tan(math.radians(fov)/2*0.35)/math.tan(math.radians(fov)/2)/0.35 * coef
    iron = math.tan(math.radians(fov)/2*0.9)/math.tan(math.radians(fov)/2)/.6 * coef
    glaz = math.tan(math.radians(fov)/2*0.3)/math.tan(math.radians(fov)/2)/0.3 * coef
else:
    acog = math.atan(coef*math.tan(math.radians(fov)/2*0.35))/math.atan(coef*math.tan(math.radians(fov)/2))/0.35
    iron = math.atan(coef*math.tan(math.radians(fov)/2*0.9))/math.atan(coef*math.tan(math.radians(fov)/2))/0.6
    glaz = math.atan(coef*math.tan(math.radians(fov)/2*0.3))/math.atan(coef*math.tan(math.radians(fov)/2))/0.3


approximations = str(Fraction(acog/iron).limit_denominator(100)).split('/')

approximations = [int(a) for a in approximations]

XFactor = acog / approximations[0]

output = '\nACOG ADS Sensitivity: {}\nIronsight ADS Sensitivity: {}'.format(approximations[0], approximations[1])

output += '\nXFactorAiming={:.6f}'.format(XFactor)

output += '\nGlaz Scope Sensitivity: {}'.format(round(glaz/XFactor))

print(output)
