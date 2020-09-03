# We will calculate the amount billed to the customer
# based on his classification code, number of days and miles driven.

# Two types of customer classification code, b and d.
# b: base charge: $40/day, mileage charge: $0.25/mile
# d: base charge: $60/day, mileage charge: $0.25 for each mile driven above 100 miles/day

print('Welcome to car rentals!')
proceed = input('Would you like to continue (y/n)? ')

while proceed == 'y':

    customer_code = input('Customer code (b or d): ')
    days = int(input('Number of days: '))
    odometer_start = int(input('Odometer reading at the start: '))
    odometer_end = int(input('Odometer reading at the end: '))
    miles_driven = odometer_end - odometer_start
    print('Miles driven:',miles_driven)

    if customer_code == 'b':
        total_price = round(40*days + 0.25*miles_driven,1)
        print('Amount due:',total_price)
    elif customer_code == 'd':
        if miles_driven > 100*days:  
            total_price = round(60*days + (miles_driven - 100*days) * 0.25,1)
            print('Amount due:',total_price)
        else:
            total_price = 60*days
            print('Amount due:',total_price)
    proceed = input('Would you like to continue (y/n)? ')
    

    
        
