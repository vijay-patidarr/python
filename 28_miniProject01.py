# creating a mini project to calculate the room rent

# input we need from the user 
print(" calculate the room rent enter following details" )

Rent = int(input("eneter total amount of rent : "))
Food  = int(input("enter total amount spendse on food :") )
Electricity_units = int(input("enter total electricity used :") )
charges_perUnit =  int(input("enter charges per units:") )
roomate_number =  int(input("enter the number of person live in room :")
)
# totling the electricity bill multiplying units and price 
Electricity_bill = Electricity_units * charges_perUnit

#calculating total expenses we done in a month 
total_expenses = Rent + Food + Electricity_bill

print(f'total expenses of the month : {total_expenses}')

# final calculation for per peroson rent 
print (f' expenses per person : {total_expenses/roomate_number}')
1