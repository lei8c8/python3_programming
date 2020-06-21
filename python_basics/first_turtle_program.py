import turtle           #allows us to use turtle library
wn = turtle.Screen()    #create a GUI window, .pgcolor() method sets the background color
alex = turtle.Turtle()  #create a turtle named alex
alex.forward(150)       #tell alex to move forward 150 units, .color() method 
alex.left(90)           #turn by 90 degrees
alex.forward(75)        #complete the 2nd side of a rectangle

alex.salary = 50000
print(alex.salary)


import turtle             # allows us to use the turtles library
wn = turtle.Screen()      # creates a graphics window
alex = turtle.Turtle()    # create a turtle named alex
alex.forward(150)         # tell alex to move forward by 150 units
alex.left(90)             # turn by 90 degrees
alex.forward(75)          # complete the second side of a rectangle
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)
wn.exitonclick()