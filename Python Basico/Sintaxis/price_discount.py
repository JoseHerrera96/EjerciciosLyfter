price = float(input("Enter the product price: $"))

discount_rate = 0.02 if price < 100 else 0.10
final_price = price - (price * discount_rate)

print("\n---")
print(f"Discount rate applied: {discount_rate * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")
