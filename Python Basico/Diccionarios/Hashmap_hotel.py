hotel = {
    "name": "Example Hotel",
    "star_count": 4,
    "rooms": [
        {"number": 101, "floor": 1, "price_per_night": 80.0},
        {"number": 202, "floor": 2, "price_per_night": 120.0},
        {"number": 303, "floor": 3, "price_per_night": 150.0},
    ],
}
# Display basic hotel information in English
print(' ')
print(f"Hotel name: {hotel['name']}")
print(f"Stars: {hotel['star_count']}")

# Calculate and display the average nightly price
prices = [room["price_per_night"] for room in hotel["rooms"]]
average_price = sum(prices) / len(prices)
print(f"Average price per night: {average_price:.2f}")