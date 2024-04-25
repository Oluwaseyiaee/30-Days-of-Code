# Calculate the Area and Volume of a Rectangle. The parameters should be collected from the user

#Area
def rec_area(length,width):

    Area = length * width
    print(Area)

# Volume
def  rec_volume(length,width, height):

    Volume =  length * width * height
    print(Volume)

#Taking input from user
length = float(input("What is the Length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))
height =float( input("What is the height of the rectangle? "))

#Calling the functions
rec_area(length,width)
rec_volume(length,width, height)