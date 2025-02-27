#Nabila Raisa, 02-27, period 1 and 2

import math
#we need math for certain operations
def sphere_volume(radius): #creating function for the sphere's volume
    volume = (4/3)* math.pi * (radius ** 3) #applying the formula of the volume of a sphere in the ways of python 
    return volume #returning the calculated volume

radius = 5 #defning that the radius is 5
result = sphere_volume(radius) #the result has the value of he function itself
print(f"1. The volume of the sphere with the radius of 5 is {result:.2f}") #Making a sentence for the function while formatting it and making sure that there is 2 decimal points


def wholesale_cost (copies): #create a function of the cost
    cover_price = 24.95 #create a variable for the cover price and a value in it
    discount= 0.40 #create a variable for the discount and a value in it
    first_copy = 3 #create a variable for the first copy and a value in it
    ship_after = 0.75 #create a variable for the later shipping price and a value in it
    discount_price = cover_price * (1-discount) #to get the discount price, we have to take the cov and multiply it with the decimal form of 40%
    total_book = discount_price * copies # to get the total books, multiply .40 with the amount of copies
    shippingcost = first_copy + (ship_after * (copies - 1)) #to get the total ship cost, add the first copy, with the ship after and multiply it with 59 copies
    total = total_book + shippingcost #the total will add the totat books and the total shipping cost
    print(f"2. The total is ${total:.2f}") #We print out how much the total is by formatting it first
    
wholesale_cost(60) #call function

def running_time (start_hour, start_minutes): #starting the function with two parameters with the hour and mins
    easy_pace = 8*60+15 #turning 8 mins into secs and adding 15 secs
    tempo_pace = 7*60+12 #trunign 7 mins into secs and adding 12 secs
    
    total_time_sec= easy_pace*2 + (tempo_pace*3) #we multiply the easy pace with 2 because it comes up twice, and tempo with 3 because they run 3 miles
    
    total_min = total_time_sec // 60 #we get the ingral division of the total mins (whole number)
    total_secs = total_time_sec % 60 #the remainder which will be the seconds
    
    end_mins = total_min + start_minutes #to get the ending minutes we add total minutes and the start minutes
    end_hour = start_hour #storing the start hour with the end hour
    
    if end_mins >= 60: #if end mins is greater or equals to 60 it will add another hour in it
        end_hour += end_mins // 60 #this shows how the minuteswill add another hour after it turns 60 mins
        end_mins = end_mins % 60 #this is for adding a minute every 60 secs
        
        return end_hour, end_mins #returns the hours and mins
    
end_hour, end_mins = running_time(6,52) #calls the function by making the 6 the hour and 52 the minutes
print (f"3. You arrive home for breakfast at {end_hour}:{end_mins} AM") #creating a sentence using formating and making it look like actual time
