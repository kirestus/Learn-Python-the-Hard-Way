#create an int named cars and give it the value of 100

#create variables
cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_cap = cars_driven * space_in_car
avg_passengers_per_car = passengers / cars_driven

#print variables
print 'there are', cars, 'cars available'
print 'there are only', drivers, 'drivers'
print 'there will be', cars_not_driven,'empty cars today'
print 'we can transport', carpool_cap, ' to carpool today'
print 'we have', passengers, 'to carpool today'
print 'we need to put about', avg_passengers_per_car, 'in each car'
