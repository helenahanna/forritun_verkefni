days_str = input('Number of days after 9/25/09: ')
days_int = int(days_str)

miles_on_reference_day = 16637000000
speed_mph = 38241
km_per_mile = 1.609344
miles_per_au = 92955887.6
miles_per_day = speed_mph * 24 #There are 24 hours in one day

distance_miles = miles_on_reference_day + miles_per_day * days_int
distance_km = km_per_mile * distance_miles
distance_au = distance_miles / miles_per_au

aproximate_distance_km = round(distance_km)
aproximate_distance_au = round(distance_au)

print('Miles from the sun:',distance_miles)
print('Kilometers from the sun:',aproximate_distance_km)
print('AU from the sun:',aproximate_distance_au)
