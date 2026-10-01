import math

#User input variables
def pick_shape(): #Get user input to decide function used
    shape = input("What shape are you working with? ")
    return shape

def get_circle_data(): #Get circle radius for functions
    r = int(input("Radius of the circle: "))
    return r

def get_square_data(): #Get square data
    pass

#Define static variables
pi = math.pi
shape = pick_shape()

# ------------ Circle functions ------------
def area_of_a_circle(r): 
    pass #Fills in the function as needed
    area = math.pow(r, 2) * pi
    print("The area of the circle is", area)

def circle_circumference(r):
    c = pi * r * 2
    print('Circumference of the circle is', c)

# ------------ Square Functions ------------
def area_of_a_square():
    pass

def perimeter_of_a_square():
    pass

#Take user input'd shape and run functions
if(shape.lower() == 'circle'):
    circle_radius = get_circle_data()
    area_of_a_circle(circle_radius)
    circle_circumference(circle_radius)
elif shape.lower() == 'square':
    area_of_a_square()
    perimeter_of_a_square()
else: print("shape invalid")