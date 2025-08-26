# week3_discount.py

# Function to calculate the final price after discount
def calculate_discount(price, discount_percent):
    """
    Returns the final price after applying discount
    if discount >= 20%, otherwise returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


# --- Main Program ---
# Get inputs from the user
price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount)

# Display results
if discount >= 20:
    print(f"The final price after {discount}% discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {price:.2f}")
