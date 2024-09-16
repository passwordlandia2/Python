#This is a practice algorithm with determining the weight of a package to see what it would cost to ship something and to calculate if they chose premium.

#Enter a fixed weight of a product:
weight = 41.5  # Example weight

print("The basic package for shipping we offer is by ground.")
print("")

# Defining the conditions of the weight to calculate different tiers of cost using an if/else/elif statement.
if weight <= 2:
    ground_cost = "Your Ground Shipping total would be $" + "{:.2f}".format(weight * 1.50 + 20.00)
elif weight > 2 and weight <= 6:
    ground_cost = "Your Ground Shipping total would be $" + "{:.2f}".format(weight * 3.00 + 20.00)
elif weight > 6 and weight <= 10:
    ground_cost = "Your Ground Shipping total would be $" + "{:.2f}".format(weight * 4.00 + 20.00)
else:
    ground_cost = "Since it's more than 10 lbs, your Ground Shipping total would be $" + "{:.2f}".format(weight * 4.75 + 20.00)

print(ground_cost)
print("")
#Premium Cost calculations and text output.
premium_ground = 125

print("And it's $" + str(premium_ground) + " extra for premium, don't forget.")

#Drone Shipping calculations
#To ensure that the shipping cost is displayed with two decimal places, you can use Python's string formatting which looks like the above and below portions. 

if weight <= 2:
    drone_cost = "your total shipping cost by drone is $" + "{:.2f}".format(weight * 4.50)
elif weight > 2 and weight <= 6:
    drone_cost = "your total shipping cost by drone is $" + "{:.2f}".format(weight * 9.00)
elif weight > 6 and weight <= 10:
    drone_cost = "your total shipping cost by drone is $" + "{:.2f}".format(weight * 12.00)
else:
    drone_cost = "since it's more than 10 lbs, your total shipping cost by drone is $" + "{:.2f}".format(weight * 14.25)

print("")

print("We also offer to ship by drone!")
print("")
print("if you chose that, then " + drone_cost)

## Now you should be able to test this all out and have it work properly, terminating to two decimals.