from math import gcd

numer = input('Enter the Numerator: ')
denom = input('Enter the Denominator: ')

# Function to reduce a fraction
# to its lowest form
def reduceFraction(x, y):
    fract_gcd = gcd(x, y)

    x = x // fract_gcd
    y = y // fract_gcd

    print(x, '/', y)


x = int(numer)
y = int(denom)

reduceFraction(x, y)
