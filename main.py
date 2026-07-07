# Simple Grocery Budget Calculator
# A basic tool to check if your wallet can cover today's shopping list.

print("--- Welcome to the Household Budget Calculator ---")

# Getting the total budget from the user safely as a float number
budget_input = input("Enter the total money you have in your pocket: ")
budget = float(budget_input)

print("\nPlease enter the prices of 3 items you want to buy today:")

# Inputting prices for three items
item1_price = float(input("Price of Item 1: "))
item2_price = float(input("Price of Item 2: "))
item3_price = float(input("Price of Item 3: "))

# Calculating the total cost
total_cost = item1_price + item2_price + item3_price

print("\n--- Shopping Budget Report ---")
print(f"Total Budget: {budget}")
print(f"Total Cost of Items: {total_cost}")

# Logic to check if money is enough
if total_cost <= budget:
    # Remaining money calculation
    change = budget - total_cost
    print("\n[Success] You have enough money!")
    print(f"Change remaining in your pocket: {change:.2f}")
else:
    # Missing money calculation
    missing_amount = total_cost - budget
    print("\n[Warning] Alert! You do not have enough money.")
    print(f"You need an extra {missing_amount:.2f} to buy these items.")

print("\nShop wisely and keep your expenses organized!")