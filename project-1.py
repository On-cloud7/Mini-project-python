#input from the user
#total rent
# total food ordered for snacking
# charge per unit
#Persons living in room or flat

#output
#total amount you've to pay is

rent = int(input("Enter the flat rent:"))
food = int (input("enter the total food ordered ="))
electricity_spent = int(input("enter the total of electricity spend:"))
charge_per_unit = int(input("enter the the charge per unit:"))
persons = int(input("enter the number of persons living in room or flat:"))

total_electricity_bill = electricity_spent*charge_per_unit
output = (rent+food+total_electricity_bill)// persons
print("each person will pay:",output)