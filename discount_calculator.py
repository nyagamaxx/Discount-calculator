# discount_calculator.py

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    A discount is applied only if discount_percent is 20% or higher.

    Parameters:
        price (float): The original price of the item
        discount_percent (float): The discount percentage to apply

    Returns:
        float: The final price after applying the discount (if applicable)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


if __name__ == "__main__":
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(price, discount_percent)

        if discount_percent >= 20:
            print(f"Discount applied! The final price is: {final_price:.2f}")
        else:
            print(f"No discount applied. The price remains: {final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
