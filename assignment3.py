def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price

price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percent: "))




final_price = calculate_discount(price, discount_percent)
if discount_percent >= 20:
    print(f"discounted price:{final_price}")
else:
    print(f"original price: {price}")
