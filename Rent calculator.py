## Inputs needed
# Rent
# Food consumed
# Electricity units used
# Charge per unit
user = str(input("Who wants to calculate their bill: "))
choice = str(input("What do you want to access: Total bill 🧾/Food 🍽️/Rent 🏠/Electricity ⚡")).lower()
if choice == "electricity":
    unit_price = float(input("Enter the price of a unit of electricity: "))
    unit_used = float(input("Enter the total units used by everyone: "))
    used_by_you = float(input("Enter the units used by you: "))
    used_percentage = (used_by_you/unit_used)*100
    bill_units = (used_percentage/100)*unit_used
    bill_electricity = bill_units*unit_price
    print("Electricity bill of", user, "is:", bill_electricity)
elif choice == "food":
    total_food = float(input("Enter amount of food ordered by everyone: "))
    food = float(input("Amount of food ordered by you: "))
    used_percentage = (food/total_food)*100
    food_bill = (used_percentage*total_food)/100
    print(f"Food bill of ", user , " is: ", food_bill, " || %payment = ", used_percentage, "%")
elif choice == "rent":
    members = int(input("How many members are there in your apartment: "))
    total_rent = float(input("Enter the total rent: "))
    rent_amount = total_rent/members
    print("Rent bill of ", user, " is: ", rent_amount)
elif choice == "total bill":
    unit_price = float(input("Enter the price of a unit of electricity: "))
    used_by_you = float(input("Enter the units used by you: "))
    bill_electricity = used_by_you * unit_price

    total_food = float(input("Enter amount of food ordered by everyone: "))
    food = float(input("Amount of food ordered by you: "))
    food_bill = (food / total_food) * total_food

    members = int(input("How many members are there in your apartment: "))
    total_rent = float(input("Enter the total rent: "))

    total = bill_electricity + food_bill + (total_rent / members)
    print("Total bill for", user, "is:", total)
else:
    print("Invalid choice.")

        
