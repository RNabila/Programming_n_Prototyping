#Nabila Raisa, Period 1 and 2, 09/20/2024

#perimeter

length= int(input("Enter a number: "))
width= int(input("Enter a number: "))
total_length_width= length + width
p= 2*total_length_width
print("Perimeter of a " + str(length) + " x " + str(width) + " rectangle is " + str(p))

#farenheit

f_temp= int(input("Enter a number: "))
sub_f= f_temp-32
celsius= sub_f*5/9
print(str(f_temp) + " degrees farenheit is " + str(celsius) + " degrees celsius")

#vertical distance

vert_velo= int(input("Enter a number: "))
time= int(input("Enter a number for time: "))
acc_grav= int(input("Enter a number for acceleration gravity: "))
vert_time= vert_velo*time
acc_time= acc_grav*time**2
v_distance= vert_time-1/2*acc_time
print("The vertical distance is " + str(v_distance))

#coordinates

x1=int(input("Enter a number: "))
x2=int(input("Enter a number: "))
y1=int(input("Enter a number: "))
y2=int(input("Enter a number: "))
x_coords= x2-x1
y_coords= y2-y1
x_squared= x_coords**2
y_squared= y_coords**2
x_and_y= x_squared + y_squared
distance= x_and_y**0.5
print("The distance is " + str(distance))













