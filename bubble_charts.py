
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  
#
#    Student no: 1822441005
#    Student name:吕家伟
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/). 
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  BUBBLE CHARTS
#
#  This task tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function,
#  "draw_bubble_chart".  You are required to complete this function
#  so that when the program is run it produces a bubble chart,
#  using data stored in a list to determine the positions and
#  sizes of the icons.  See the instruction sheet accompanying this
#  file for full details.
#
#--------------------------------------------------------------------#  



#-----Preamble and Test Data-----------------------------------------#
#
#

# Module provided
#
# You may use only the turtle graphics functions for this task;
# you may not import any other modules or files.

from turtle import *


# Given constants
#
# These constant values are used in the main program that sets up
# the drawing window; do not change any of these values.

max_value = 350 # maximum positive or negative value on the chart
margin = 25 # size of the margin around the chart
legend_width = 400 # space on either side of the window for the legend
window_height = (max_value + margin) * 2 # pixels
window_width = (max_value + margin) * 2 + legend_width # pixels
font_size = 12 # size of characters on the labels in the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
tick_size = 5 # size of the ticks on either side of the axes, in pixels


# Test data
#
# These are the data sets that you will use to test your code.
# Each of the data sets is a list containing the specifications
# for several icons ("bubbles") to display on the screen.  Each
# such list element specifies one icon using four values:
#
#    [icon_style, x_value, y_value, z_value]
#
# The 'icon_style' is a character string specifying which icon to
# to display.  Possible icons are named 'Icon 0' to 'Icon 4'.
# The final three values are integers specifying the icon's values
# in three dimensions, x, y and z.  The x and y values will be in
# the range -350 to 350, and determine where to place the icon on
# the screen.  The z value is in the range 0 to 350, and determines
# how big the icon must be (i.e., its widest and/or highest size on
# the screen, in pixels).

# The first icon in three different sizes
data_set_00 = [['Icon 0', -200, 200, 20],
               ['Icon 0', 200, 200, 120],
               ['Icon 0', 0, 0, 100]]

# The second icon in four different sizes
data_set_01 = [['Icon 1', -200, 200, 20],
               ['Icon 1', 200, 200, 120],
               ['Icon 1', 200, -200, 60],
               ['Icon 1', 0, 0, 100]]

# The third icon in five different sizes
data_set_02 = [['Icon 2', -200, 200, 300],
               ['Icon 2', -200, -200, 30],
               ['Icon 2', 200, -200, 90],
               ['Icon 2', 200, 200, 120],
               ['Icon 2', 0, 0, 100]]

# The fourth icon in four different sizes
data_set_03 = [['Icon 3', -200, 200, 300],
               ['Icon 3', -200, -200, 30],
               ['Icon 3', 200, -200, 90],
               ['Icon 3', 0, 0, 100]]

# The fifth icon in four different sizes
data_set_04 = [['Icon 4', 200, 200, 190],
               ['Icon 4', -200, -200, 10],
               ['Icon 4', 200, -200, 90],
               ['Icon 4', 0, 0, 100]]

# The next group of data sets test all five of your icons
# at the same time

# All five icons at the same large size
data_set_05 = [['Icon 0', -200, 200, 200],
               ['Icon 1', 200, 200, 200],
               ['Icon 2', 200, -200, 200],
               ['Icon 3', -200, -200, 200],
               ['Icon 4', 0, 0, 200]]

# All five icons at another size, listed in a different order
data_set_06 = [['Icon 4', 0, 0, 150],
               ['Icon 3', -200, -200, 150],
               ['Icon 2', -200, 200, 150],
               ['Icon 1', 200, 200, 150],
               ['Icon 0', 200, -200, 150]]

# All five icons arranged diagonally, at increasing sizes
data_set_07 = [['Icon 0', -200, -200, 15],
               ['Icon 1', -100, -100, 50],
               ['Icon 2', 0, 0, 100],
               ['Icon 3', 100, 100, 120],
               ['Icon 4', 200, 200, 180]]

# An extreme test in which all five icons are VERY small
data_set_08 = [['Icon 0', -100, -80, 5],
               ['Icon 2', 100, -100, 1],
               ['Icon 3', 10, 30, 2],
               ['Icon 1', 100, 100, 0],
               ['Icon 4', 200, 200, 4]]

# The next group of data sets are intended as "realistic" ones
# in which all five icons appear once each at various sizes in
# different quadrants in the chart

# Data occurs in all four quadrants
data_set_09 = [['Icon 0', -265, -80, 50],
               ['Icon 2', 100, -146, 78],
               ['Icon 3', -50, 130, 69],
               ['Icon 1', 210, 100, 96],
               ['Icon 4', 200, 300, 45]]

# All data appears in the top quadrants
data_set_10 = [['Icon 4', -265, 80, 140],
               ['Icon 2', 100, 146, 24],
               ['Icon 1', 10, 30, 99],
               ['Icon 0', 210, 100, 75],
               ['Icon 3', 200, 300, 65]]

# All data appears in the top right quadrant
data_set_11 = [['Icon 3', 265, 80, 140],
               ['Icon 1', 100, 146, 24],
               ['Icon 2', 20, 30, 109],
               ['Icon 4', 210, 205, 75],
               ['Icon 0', 200, 300, 65]]

# All data appears in the bottom left quadrant
data_set_12 = [['Icon 2', -265, -110, 130],
               ['Icon 3', -100, -146, 34],
               ['Icon 0', -25, -40, 73],
               ['Icon 1', -210, -200, 75],
               ['Icon 4', -180, -320, 65]]

# Another case where data appears in all four quadrants
data_set_13 = [['Icon 4', -265, 80, 96],
               ['Icon 3', 100, -46, 54],
               ['Icon 2', 50, 30, 89],
               ['Icon 1', -210, -190, 75],
               ['Icon 0', 250, 300, 123]]

# Yet another set with data in all four quadrants
data_set_14 = [['Icon 1', 212, -165, 90],
               ['Icon 2', 153, -22, 125],
               ['Icon 3', 84, 208, 124],
               ['Icon 4', -105, -58, 85],
               ['Icon 0', -62, 274, 57]]

# A random test - it produces a different data set each time you run
# your program!
from random import randint
max_rand_coord = 300
min_size, max_size = 20, 200

data_set_15 = [[icon,
                randint(-max_rand_coord, max_rand_coord),
                randint(-max_rand_coord, max_rand_coord),
                randint(min_size, max_size)]
               for icon in ['Icon 0', 'Icon 1', 'Icon 2', 'Icon 3', 'Icon 4']]

# Finally, just for fun, a random test that produces a montage
# by plotting each icon twenty times (which obviously doesn't
# make sense as a real data set)
data_set_16 = [[icon,
                randint(-max_rand_coord, max_rand_coord),
                randint(-max_rand_coord, max_rand_coord),
                randint(min_size, max_size)]
               for icon in ['Icon 0', 'Icon 1', 'Icon 2', 'Icon 3', 'Icon 4'] * 20]

#***** If you want to create your own test data sets put them here

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the task by replacing the dummy function below with
#  your code

def draw_bubble_chart(data_set):
 
    colormode(255)        ##Format RGB color


##  draw Mitsubishi picture
    def draw_Icon0(x_coordinate,y_coordinate,size):  ## afferent location and size
        penup()
        goto(x_coordinate,y_coordinate)   ## go to it's location
        seth(0)
        pendown()

        pencolor('red')
        fillcolor('red')
## set it's pencolor and fill color

        begin_fill()
        seth(90)
        right(30)
        fd(size*0.385)
        left(60)
        fd(size*0.385)
        left(120)
        fd(size*0.385)
        left(60)
        fd(size*0.385)
        end_fill()
## draw first rhombus
        seth(180)
        begin_fill()
        fd(size*0.385)
        left(60)
        fd(size*0.385)
        left(120)
        fd(size*0.385)
        left(60)
        fd(size*0.385)
        end_fill()
## draw second rhombus
        seth(0)
        begin_fill()
        fd(size*0.385)
        right(60)
        fd(size*0.385)
        right(120)
        fd(size*0.385)
        right(60)
        fd(size*0.385)
        end_fill()
## draw third rhombus
    
##   draw Volkswagen picture
    def draw_Icon1(x_coordinate,y_coordinate,size):## afferent location and size
        penup()
        goto(x_coordinate,y_coordinate)
        seth(-90)
        fd(size/2)        ## go to it's location
        seth(0)
        pendown()

        pencolor('blue')
        pensize(size/2*0.15)
## format painting brush


        circle(size/2)
        penup()
        seth(90)
        fd(size/2)
        pendown()
        color('white')
        dot(size*0.9)
        color('blue')
        dot(size*0.8)

## draw word 'V'
        penup()
        goto(x_coordinate,y_coordinate)
        pendown()
        pensize(size/2*0.15)
        pencolor('white')
        seth(110)
        fd(size*0.4)
        penup()
        goto(x_coordinate,y_coordinate)
        pendown()
        seth(70)
        fd(size*0.4)

## draw word 'W'
        penup()
        goto(x_coordinate,y_coordinate)
        pendown()
        right(180)
        fd(size*0.4)
        seth(110)
        fd(size*0.6)
        penup()
        goto(x_coordinate,y_coordinate)
        pendown()
        right(180)
        fd(size*0.4)
        seth(70)
        fd(size*0.6)

        penup()
        goto(x_coordinate,y_coordinate)
        pendown()
        pensize(size/2*0.15*0.4)
        pencolor('blue')
        seth(0)
        fd(size*0.1)
        seth(180)
        fd(size/4)



## draw BMW picture
    def draw_Icon2(x_coordinate,y_coordinate,size): ## afferent location and size
        penup()
        goto(x_coordinate,y_coordinate)    ## go to it's location
        pendown()

        color('silver')
        dot(size)
        color('black')
        dot(size*19/20)
        color('white')
        dot(size*11/20)
## draw frame
        pensize(0)
        color('black')
        fillcolor('blue')
        begin_fill()
        seth(180)
        fd(size*11/40)
        seth(-90)
        circle(size*11/40,-90)
        seth(270)
        fd(size*11/40)
        end_fill()
## draw BMW part 'blue'
        fillcolor('blue')
        begin_fill()
        seth(270)
        fd(size*11/40)
        seth(0)
        circle(size*11/40,90)
        seth(180)
        fd(size*11/40)
        end_fill()

## draw word 'B'
        penup()
        goto(x_coordinate-(size*9/40),y_coordinate+size/5)
        pendown()
        pensize(size*0.022)
        seth(140)
        pencolor('white')
        fd(size*0.14)
        seth(45)
        fd(size*0.1)
        seth(0)
        circle(-size/20,90)
        seth(225)
        fd(size*0.09)
        penup()
        seth(45)
        fd(size*0.1)
        pendown()
        seth(0)
        circle(-size/20,90)
        seth(225)
        fd(size*0.09)

## draw word 'M'
        penup()
        goto(x_coordinate-size*0.06,y_coordinate+size*0.3)
        pendown()
        seth(90)
        fd(size*0.135)
        seth(-66)
        fd(size*0.145)
        seth(66)
        fd(size*0.145)
        seth(-90)
        fd(size*0.135)

## draw word 'W'
        penup()
        goto(x_coordinate+size*0.175,y_coordinate+size/4)
        pendown()
        seth(60)
        fd(size*0.14)
        penup()
        goto(x_coordinate+size*0.175,y_coordinate+size/4)
        pendown()
        seth(30)
        fd(size*0.14)
        seth(-115)
        fd(size*0.14)
        seth(30)
        fd(size*0.14)



## draw benz picture
    def draw_Icon3(x_coordinate,y_coordinate,size):## afferent location and size
        penup()
        goto(x_coordinate,y_coordinate)
        seth(-90)
        fd(size/2)                     ## go to it's location
        seth(0)
        pendown()

        pensize(size/2*0.08)
        pencolor((233,233,216))
        ## format painting brush

## draw triangle
        circle(size/2)
        pensize(size/2*0.01)
        fillcolor((233,233,216))
        begin_fill()
        penup()
        seth(90)
        fd(size)
        pendown()
        seth(-95)
        fd(size/2*0.95)
        right(50)
        fd(size/2*0.95)
        left(170)
        fd(size/2*0.95)
        right(50)
        fd(size/2*0.95)
        left(170)
        fd(size/2*0.95)
        right(50)
        fd(size/2*0.95)
        end_fill()

## draw audi picture
    def draw_Icon4(x_coordinate,y_coordinate,size):## afferent location and size
        penup()
        goto(x_coordinate,y_coordinate)
        seth(0)
        fd(size/8)
        seth(-90)
        fd(size/8)   ## go to it's location
        seth(0)
        pendown()

        pensize(size/4*0.1)
        pencolor((233,233,216))
## format painting brush

## draw first round
        circle(size/8)
        penup()
        fd(size/8*1.4)
        pendown()
## draw second round
        circle(size/8)
        penup()
        seth(180)
        fd(size/4*1.4)
        pendown()
## draw third round
        circle(-size/8)
        penup()
        fd(size/8*1.4)
        pendown()
## draw fourth round
        circle(-size/8)
        



#Read coordinates and sizes of icons
    for row in data_set:  
        Icon_no = row[0]
        if Icon_no == 'Icon 0':
            Icon0_x = row[1]
            Icon0_y = row[2]
            Icon0_size = row[3]
            draw_Icon0(Icon0_x,Icon0_y,Icon0_size)
            ## Call the drawing function and pass in parameters
        elif Icon_no == 'Icon 1':
            Icon1_x = row[1]
            Icon1_y = row[2]
            Icon1_size = row[3]
            draw_Icon1(Icon1_x,Icon1_y,Icon1_size)
            ## Call the drawing function and pass in parameters
        if Icon_no == 'Icon 2':
            Icon2_x = row[1]
            Icon2_y = row[2]
            Icon2_size = row[3]
            draw_Icon2(Icon2_x,Icon2_y,Icon2_size)
            ## Call the drawing function and pass in parameters
        if Icon_no == 'Icon 3':
            Icon3_x = row[1]
            Icon3_y = row[2]
            Icon3_size = row[3]
            draw_Icon3(Icon3_x,Icon3_y,Icon3_size)
            ## Call the drawing function and pass in parameters
        if Icon_no == 'Icon 4':
            Icon4_x = row[1]
            Icon4_y = row[2]
            Icon4_size = row[3]
            draw_Icon4(Icon4_x,Icon4_y,Icon4_size)
            ## Call the drawing function and pass in parameters

## draw legend
    def draw_legend():
        penup()
        goto(400,200)
        pendown()

        pencolor('black')
        pensize(1)
        seth(-90)
        fd(400)
        seth(0)
        fd(200)
        seth(90)
        fd(400)
        seth(-180)
        fd(200)

        penup()
        seth(-45)
        fd(45)
        pendown()
        seth(0)

## write title
        write('Automobile makes ',font=("微软雅黑",12,"normal"))

## draw five icons
        draw_Icon0(440,110,60)
        draw_Icon1(440,50,60)
        draw_Icon2(440,-20,60)
        draw_Icon3(440,-90,60)
        draw_Icon4(440,-150,70)

## write each icons' name
        pencolor('black')
        penup()
        goto(500,110)
        pendown()
        write('Mitsubishi',font=("微软雅黑",11,"normal"))

        penup()
        goto(500,40)
        pendown()
        write('Volkswagen',font=("微软雅黑",11,"normal"))

        penup()
        goto(500,-28)
        pendown()
        write('BMW',font=("微软雅黑",11,"normal"))

        penup()
        goto(500,-100)
        pendown()
        write('Benz',font=("微软雅黑",11,"normal"))

        penup()
        goto(500,-160)
        pendown()
        write('Audi',font=("微软雅黑",11,"normal"))




    draw_legend()    ## Call the function to draw the legend
    

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the drawing environment, ready for you
# to start drawing your bubble chart.  Do not change any of
# this code except the lines marked '*****'
    
# Set up the drawing window with enough space for the grid and
# legend
setup(window_width+200,window_height)
title('Bubble Chart') #***** Choose a title appropriate to your icons

# Draw as quickly as possible by minimising animation
hideturtle()     #***** You may comment out this line while debugging
                 #***** your code, so that you can see the turtle move
speed('fastest') #***** You may want to slow the drawing speed
                 #***** while debugging your code

# Choose a neutral background colour                    
bgcolor('grey')

# Draw the two axes
pendown() # assume we're at home, facing east
forward(max_value)
left(180) # face west
forward(max_value * 2)
home()
setheading(90) # face north
forward(max_value)
left(180) # face south
forward(max_value * 2)
penup()

# Draw each of the tick marks and labels on the x axis
for x_coord in range(-max_value, max_value + 1, grid_size):
    if x_coord != 0: # don't label zero
        goto(x_coord, -tick_size)
        pendown()
        goto(x_coord, tick_size)
        penup()
        write(str(x_coord), align = 'center',
              font=('Arial', font_size, 'normal'))
        
# Draw each of the tick marks and labels on the y axis
for y_coord in range(-max_value, max_value + 1, grid_size):
    if y_coord != 0: # don't label zero
        goto(-tick_size, y_coord)
        pendown()
        goto(tick_size, y_coord)
        penup()
        goto(tick_size, y_coord - font_size / 2) # Allow for character height
        write('  ' + str(y_coord), align = 'left',
              font=('Arial', font_size, 'normal'))

# Call the student's function to display the data set
draw_bubble_chart(data_set_05) #***** Change this for different data sets
    
# Exit gracefully
hideturtle()
done()

#
#--------------------------------------------------------------------#




