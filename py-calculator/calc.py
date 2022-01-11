import time
import random
import sys
import matplotlib.pyplot as plt
from fractions import Fraction

amountOfBuffers = random.randint(1,5)

for buffers in range(0,amountOfBuffers):
    print("Loading...Please Wait")
    time.sleep(0.5)

print("Welcome. Please enter a calculator function with the corresponding number to continue")

time.sleep(1)

print("1 - Equation of a linear line")
print("2 - Equation of a Perpendicular Bisector")


calcChoice = input()

calcOptions = {
    "1" : "equationOfALine",
    "2" : "equationOfAPerpendicular"

}

calcChoice = str(calcChoice)

if calcOptions[calcChoice] == "equationOfALine":

    print("Enter the first pair of coordinates")
    coord1 = input()
    print("Enter the second pair of coordinates")
    coord2 = input()

    coord1 = coord1.split(",")
    coord2 = coord2.split(",")
    
    x1 = int(coord1[0])
    x2 = int(coord2[0])

    y1 = int(coord1[1])
    y2 = int(coord2[1])

    if x1 == x2:
        print("Error. Slope is vertical")
        sys.exit()
        

    amountOfBuffers = random.randint(1,5)

    for buffers in range(0,amountOfBuffers):
        print("Calculating...Please Wait")
        time.sleep(0.5)


    gradientNumerator = y1 - y2
    gradientDenominator = x1 - x2
    gradient = gradientNumerator/gradientDenominator

    gradient_fraction = (gradient).as_integer_ratio()

    mx = x1 * gradient

    mx = mx * -1
    b = y1 + mx
    equation = f"y = {gradient_fraction[0]}/{gradient_fraction[1]}x + {b}"

    x_digits = [x1,x2]
    y_digits = [y1,y2]

    plt.plot(x_digits, y_digits)

    plt.xlabel('x - axis')

    plt.ylabel('y - axis')

    plt.title(equation)

    plt.show()

    sys.exit()


elif calcOptions[calcChoice] == "equationOfAPerpendicular":

    print("Enter the first pair of coordinates")
    coord1 = input()
    print("Enter the second pair of coordinates")
    coord2 = input()

    coord1 = coord1.split(",")
    coord2 = coord2.split(",")
    
    x1 = int(coord1[0])
    x2 = int(coord2[0])

    y1 = int(coord1[1])
    y2 = int(coord2[1])

    if x1 == x2:
        print("Error. Slope is vertical")
        sys.exit()
        

    amountOfBuffers = random.randint(1,5)

    for buffers in range(0,amountOfBuffers):
        print("Calculating...Please Wait")
        time.sleep(0.5)


    gradientNumerator = y1 - y2
    gradientDenominator = x1 - x2
    gradient = gradientNumerator/gradientDenominator

    gradient_fraction = (gradient).as_integer_ratio()

    mx = x1 * gradient

    mx = mx * -1
    b = y1 + mx
    equation = f"y = {gradient_fraction[0]}/{gradient_fraction[1]}x + {b}"

    gradient_2 = -gradient_fraction[1]/gradient_fraction[0]

    gradient_2_fraction = (gradient_2).as_integer_ratio()

    midpoint_x = (x1+x2)/2
    midpoint_y = (y1+y2)/2

    mx = midpoint_x * gradient_2

    mx = mx * -1
    b = midpoint_y + mx
    equation_2 = f"y = {gradient_2_fraction[0]}/{gradient_2_fraction[1]}x + {b}"

    x_digits = [x1,x2]
    y_digits = [y1,y2]

    x_2_digits = [midpoint_x, midpoint_x + gradient_2_fraction[1]]
    y_2_digits = [midpoint_y, midpoint_y + gradient_2_fraction[0]]

    plt.plot(x_digits, y_digits)
    plt.plot(x_2_digits, y_2_digits)

    plt.xlabel('x - axis')

    plt.ylabel('y - axis')

    plt.title(f"{equation}\n{equation_2}")

    plt.show()

    sys.exit()

    

